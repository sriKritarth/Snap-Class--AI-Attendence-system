<div align="center">

<img src="https://snap-class-frontend-deploy.vercel.app/static/img/logo.png" alt="SnapClass Logo" width="120"/>

# Snap-Class — AI Attendance System

### Making Attendance Faster Using AI

**Revolutionizing the classroom with next-gen computer vision and voice biometrics.**  
Trusted by educators for speed, accuracy, and security.

[![Landing Page](https://img.shields.io/badge/🌐%20Landing%20Page-Visit-blue?style=for-the-badge)](https://snap-class-frontend-deploy.vercel.app/)
[![Live App](https://img.shields.io/badge/🚀%20Live%20App-Open%20SnapClass-brightgreen?style=for-the-badge)](https://snapclass-main-view.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase)](https://supabase.com/)

</div>

---

## 🔗 Live Deployment

| Resource | URL |
|---|---|
| 🌐 **Landing Page** | [snap-class-frontend-deploy.vercel.app](https://snap-class-frontend-deploy.vercel.app/) |
| 🚀 **AI Attendance App** | [snapclass-main-view.streamlit.app](https://snapclass-main-view.streamlit.app/) |

> The landing page serves as the product's entry point. Clicking **"Start AI Attendance"** on the landing page takes users directly into the live Streamlit application.

---

## 🧠 Overview

**Snap-Class** is an AI-powered classroom attendance system that eliminates the need for manual roll-calls. It combines three cutting-edge methods to mark attendance automatically:

- 📸 **AI Face Analysis** — advanced neural networks identify every student from a single class photo in milliseconds
- 🎙️ **Sequential Voice ID** — audio-AI matches each student's voice biometrics against stored embeddings in real-time
- 📱 **QR-Driven Roster** — course codes generate unique QR codes for instant, zero-friction student enrollment

The platform is split into two dedicated role-based interfaces: a **Teacher portal** for managing classes and triggering AI sessions, and a **Student portal** for biometric registration and attendance tracking.

---

## ✨ Features at a Glance

### 👩‍🏫 For Teachers
- Secure login with encrypted, synced session management
- Interactive dashboard to manage subjects, rosters, and attendance logs
- One-click course creation with auto-generated QR enrollment codes
- AI Face Attendance — scan an entire room from a single photo
- AI Voice Attendance — futuristic sequential voice roll-call
- Actionable records with **confidence scores**, CSV export, and long-term trend tracking

### 🎓 For Students
- Instant class enrollment via QR code or teacher-shared join link
- One-time **Face ID** and **Voice ID** biometric registration
- Personal attendance dashboard showing percentage per subject in real-time
- Auto-enrollment triggered automatically when accessing via a `?join-code=` URL

---

## 🖼️ Screenshots & Demo

### Landing Page
![Landing Page](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-landing.png)

### Teacher — FaceID Attendance Session
![FaceID Attendance](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-teacher-flow-5.2-photo-attendance.png)

### Teacher — Voice Attendance Session
![Voice Attendance](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-teacher-flow-5.1-voice-attendance.png)

### Teacher — Dashboard
![Teacher Dashboard](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-teacher-flow-2-dashboard.png)

### Teacher — Attendance Records
![Attendance Records](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-teacher-flow-5-see-stored-records.png)

### Student — Enrollment
![Student Enrollment](https://snap-class-frontend-deploy.vercel.app/static/img/demo/snap-student-flow-2-enroll.png)

### Student — Personal Dashboard
![Student Dashboard](https://snap-class-frontend-deploy.vercel.app/static/img/demo/student-scan.png)

---

## 🗺️ User Journeys

### 👩‍🏫 The Teacher's Journey

| Step | Stage | Description |
|---|---|---|
| 01 | **Secure Login** | Start your session through the high-security authentication portal. Data is encrypted and synced across all devices. |
| 02 | **Interactive Dashboard** | Manage all subjects, attendance logs, and student rosters from a single unified stream. |
| 03 | **Course Management** | Create a new subject — SnapClass auto-generates a QR code and everything needed to start tracking instantly. |
| 04 | **FaceID Attendance** | Upload or capture a class photo. Computer vision scans the room and identifies every student in milliseconds. |
| 05 | **Voice ID Attendance** | Switch to voice mode. Students say "Present" one by one, and the AI matches their unique voice signature in real-time. |
| 06 | **Actionable Records** | Review historical logs, view AI confidence scores, download CSV reports, and monitor long-term attendance trends. |

### 🎓 The Student's Journey

| Phase | Stage | Description |
|---|---|---|
| 01 | **Instant Enrollment** | Join a course in seconds using the teacher-shared QR code or join link — no tedious sign-up forms. |
| 02 | **Biometric Registration** | Register Face ID and Voice ID once. The AI securely stores these biometrics for all future class sessions. |
| 03 | **Personal Dashboard** | A unified view to track attendance percentage across all subjects and receive real-time updates. |

---

## 🗂️ Project Structure

```
Snap-Class--AI-Attendence-system/
│
├── app.py                        # Main entry point — Streamlit app with role-based routing
├── requirements.txt              # Python dependencies
├── .streamlit/                   # Streamlit theme & server config
│   └── config.toml
│
└── src/
    ├── screens/
    │   ├── home_screen.py        # Landing/login page — role selector (Teacher / Student)
    │   ├── teacher_screen.py     # Full teacher dashboard, course & attendance management
    │   └── student_screen.py     # Student dashboard, biometric registration & tracking
    │
    └── components/
        └── auto_enroll_dialog.py # QR / join-code auto-enrollment dialog for students
```

**Routing Logic (`app.py`):** The app reads `st.session_state['login_type']` and routes to `teacher_screen`, `student_screen`, or `home_screen`. A `?join-code=<code>` query parameter auto-triggers the student login flow and the enrollment dialog.

---

## 🛠️ Tech Stack

| Layer | Technology | Role |
|---|---|---|
| **UI / App** | [Streamlit](https://streamlit.io/) | Reactive web app framework |
| **Landing Page** | HTML / CSS / JS (Vercel) | Product marketing & app entry point |
| **Face Recognition** | `dlib`, `face_recognition_models`, `scikit-learn` | High-fidelity facial biometrics |
| **Voice Recognition** | [Resemblyzer](https://github.com/resemble-ai/Resemblyzer), [Librosa](https://librosa.org/) | Unique student voice embeddings |
| **Image Processing** | `Pillow`, `NumPy` | Photo preprocessing before recognition |
| **Data Handling** | `Pandas`, `NumPy` | Attendance records & data analysis |
| **Database & Auth** | [Supabase](https://supabase.com/) | PostgreSQL + Cloud Storage + Auth |
| **Password Security** | `bcrypt` | Secure credential hashing |
| **QR Code** | `segno` | Enrollment QR code generation |
| **App Hosting** | [Streamlit Community Cloud](https://streamlit.io/cloud) | Live app deployment |
| **Landing Hosting** | [Vercel](https://vercel.com/) | Landing page deployment |
| **Language** | Python 3 (100%) | Entire backend & app logic |

---

## 🚀 Deployment

### App — Streamlit Community Cloud

The Streamlit application is live at:  
👉 **[snapclass-main-view.streamlit.app](https://snapclass-main-view.streamlit.app/)**

To deploy your own instance:
1. Push your code to a public GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io/) and connect your repo.
3. Set `app.py` as the main file entry point.
4. Add your Supabase credentials under **App Settings → Secrets**.

### Landing Page — Vercel

The marketing landing page is live at:  
👉 **[snap-class-frontend-deploy.vercel.app](https://snap-class-frontend-deploy.vercel.app/)**

The **"Start AI Attendance"** CTA button on the landing page links directly to the deployed Streamlit app, creating a seamless user flow from the marketing site into the product.

To deploy the landing page:
1. Push the frontend source code to a GitHub repository.
2. Import the project at [vercel.com](https://vercel.com/).
3. Vercel auto-detects the framework and deploys on every push to `main`.

---

## ⚙️ Local Setup

### Prerequisites

- Python 3.9+
- A [Supabase](https://supabase.com/) project (free tier works)
- `cmake` and a C++ compiler (required by `dlib`)

### 1. Clone the Repository

```bash
git clone https://github.com/sriKritarth/Snap-Class--AI-Attendence-system.git
cd Snap-Class--AI-Attendence-system
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

> **Important:** `dlib` requires `cmake` and C++ build tools installed on your system before running pip install.

```bash
pip install "setuptools<70.0.0"
pip install -r requirements.txt
```

### 4. Configure Supabase Secrets

Create `.streamlit/secrets.toml` with your Supabase credentials:

```toml
[supabase]
url = "https://your-project-id.supabase.co"
key = "your-anon-public-key"
```

> ⚠️ Never commit `secrets.toml` to version control. Add it to `.gitignore`.

### 5. Run the App

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## 📦 Dependencies

```txt
# Frontend
streamlit
numpy
pandas

# Face recognition
scikit-learn
dlib-bin
git+https://github.com/ageitgey/face_recognition_models
setuptools<70.0.0

# Database & Auth
supabase
bcrypt

# QR code generator
segno

# Image preprocessing
pillow

# Voice recognition
librosa
resemblyzer
```

---

## 🔐 Secrets Reference

| Key | Description |
|---|---|
| `supabase.url` | Your Supabase project URL |
| `supabase.key` | Your Supabase anon/public API key |

---

## 🤝 Contributing

Contributions are very welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: describe your change"`
4. Push to your fork: `git push origin feature/your-feature`
5. Open a Pull Request

---

## ⚠️ Known Limitations

- **`dlib` installation** can be challenging on some platforms. Ensure `cmake` and a C++ compiler are installed first.
- **Face recognition accuracy** may degrade under poor or inconsistent lighting conditions.
- **Voice recognition** works best in quiet environments; background noise can affect matching accuracy.
- `setuptools` is pinned below `70.0.0` due to a known compatibility constraint with `dlib`.

---

## 📄 License

This project is open source. See the repository for license details.

---

## 👨‍💻 Author

**sriKritarth**  
GitHub: [@sriKritarth](https://github.com/sriKritarth)

---

<div align="center">

🌐 [Landing Page](https://snap-class-frontend-deploy.vercel.app/) &nbsp;|&nbsp; 🚀 [Live App](https://snapclass-main-view.streamlit.app/)

⭐ Star this repo if you find it useful!

*© 2026 SnapClass AI. Built with ❤️ for educators everywhere.*

</div>