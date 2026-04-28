from src.db.config import supabase
import bcrypt


def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode() , bcrypt.gensalt()).decode()


def check_pass(pwd , hashed_pwd):
    return bcrypt.checkpw(pwd.encode() , hashed_pwd.encode())

def check_teacher_exists(username):
    #username should be unique
    response = supabase.table("teachers").select("username").eq("username" ,username).execute()
    return len(response.data) > 0


def create_teacher(username , password , name):
    data = {'username' : username , 'password' : hash_pass(password) , 'name' : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data



def teacher_login(username , password):
    response = supabase.table("teachers").select("*").eq("username" , username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password , teacher['password']):
            return teacher #Returns true or false
    return None


def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def create_student(new_name , face_emb = None , voice_emb = None):
    data = {"name" : new_name , "face_embeddings" : face_emb , "voice_embeddings" : voice_emb}
    response = supabase.table("students").insert(data).execute()
    return response.data

def create_subject(subject_code , sub_name , section , teacher_id):
    data = {"subject_code" : subject_code , "name" :sub_name , "section" : section , "teacher_id" : teacher_id}
    response = supabase.table("subject").insert(data).execute()
    return response.data

def get_teacher_subject(teacher_id):
    response = supabase.table("subject").select("* , subject_students(count) , attendance_logs(timestamp)").eq("teacher_id" , teacher_id).execute()
    subject = response.data

    for sub in subject:
        sub['total_students'] = sub.get("subject_students" , [{}])[0].get('count' , 0) if sub.get("subject_students") else 0
        attendance = sub.get('attendance_logs' , [])
        unique_session = len(set(log['timestamp'] for log in attendance))
        sub['total_classes'] = unique_session


        sub.pop("subject_students",  None)
        sub.pop("attendance_logs" , None)

    return subject

def enroll_student_to_subject(student_id ,  subject_id):
    data = {"subject_id": subject_id , "student_id" : student_id}
    res = supabase.table('subject_students').insert(data).execute()
    return res.data


def unenroll_student_to_subject(student_id ,  subject_id):
    res = supabase.table('subject_students').delete().eq("subject_id" , subject_id).eq("student_id" , student_id).execute()
    return res.data

def get_students_subject(student_id):
    response = supabase.table("subject_students").select("* , subject(*)").eq("student_id" ,student_id).execute()
    return response.data

def get_students_attendance(student_id):
    response = supabase.table("attendance_logs").select("* , subject(*)").eq("student_id" ,student_id).execute()
    return response.data

def create_attendance(logs):
    response = supabase.table('attendance_logs').insert(logs).execute()
    return response.data

def get_attendance_for_teacher(teacher_id):
    response = supabase.table('attendance_logs').select("* , subject!inner(*)").eq("subject.teacher_id" , teacher_id).execute()
    return response.data