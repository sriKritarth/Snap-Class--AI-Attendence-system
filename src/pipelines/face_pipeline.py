import numpy as np
import dlib 
from sklearn.svm import SVC
import face_recognition_models
import streamlit as st

from src.db.db import get_all_students


@st.cache_resource
def load_dlib_models():
    #detects face

    detector = dlib.get_frontal_face_detector() 

    #Predicts the shape of the face and the landmarks
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    #helps in Creating embedding of the detected face
    face_recog = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector , sp , face_recog


def get_embeddings(image_np):
    detector , sp , facerec = load_dlib_models()
    faces = detector(image_np , 1)

    encodings = []

    for face in faces :
        shape = sp(image_np , face)
        embed_face = facerec.compute_face_descriptor(image_np , shape , 1)

        encodings.append(np.array(embed_face))

    return encodings


@st.cache_resource
def get_trained_model():
    x = [] #Embeddings
    y = [] #id

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:
        embedding = student['face_embeddings']

        if embedding:
            x.append(np.array(embedding))
            y.append(student['student_id'])

    if len(x) == 0:
        return 0
    
    clf = SVC(kernel='linear' , probability = True , class_weight='balanced')

    try:
        clf.fit(x , y)
    except ValueError:
        pass 

    return {"clf" : clf , 'X' : x , 'Y' : y}


def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(image_np):
    encodings = get_embeddings(image_np=image_np)
    detected_students = {}

    model_data = get_trained_model()
    
    if not model_data:
        return detected_students , [] , len(encodings)
    
    clf = model_data["clf"]
    x_train = model_data['X']
    y_train = model_data['Y']

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        if len(all_students) >= 2:
            predicted_id = int(clf.predict([encoding])[0])

        else:
            predicted_id = int(all_students[0])

    
        student_embeddings = x_train[y_train.index(predicted_id)]

        #Evaluation
        best_match_score = np.linalg.norm(student_embeddings - encoding)

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:
            detected_students[predicted_id] = True

    return detected_students , all_students , len(encodings)