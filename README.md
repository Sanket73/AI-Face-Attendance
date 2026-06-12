# SnapClass — AI Powered Attendance System

> Revolutionizing the classroom with next-gen computer vision and voice biometrics.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Vercel-black?style=flat-square&logo=vercel)](https://ai-sc-landing-page.vercel.app/)
[![App](https://img.shields.io/badge/Launch%20App-Streamlit-FF4B4B?style=flat-square&logo=streamlit)](https://ai-face-attendance-main.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)

---

## What is SnapClass?

**SnapClass** is an AI-powered attendance management system built for modern classrooms. Instead of calling roll manually, teachers snap a single class photo and SnapClass's facial recognition AI marks every student present in milliseconds. Alternatively, students can speak a single word in voice mode and the system matches their unique voice signature in real time.

This repository contains the **marketing landing page** for SnapClass — a Flask-based web app deployed on Vercel that presents the product's features, teacher and student journeys, and tech stack.

---

## ✨ Core Features (Product)

| Feature | Description |
|---|---|
| 📸 **AI Face Analysis** | Advanced neural networks identify every student from a single class photo |
| 🎙️ **Sequential Voice ID** | Students say "Present" and audio-AI matches their voice biometric in real time |
| 📱 **QR-Driven Enrollment** | Course codes generate unique QR codes — zero manual data entry |
| ☁️ **Cloud Records** | Historical logs with confidence scores and downloadable CSV reports via Supabase |
| 🔐 **Secure Auth** | Encrypted sessions synced across devices |

---

## 🗂️ Project Structure

```
ai-sc-landing-page/
├── app.py              # Flask entry point — serves the landing page
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Jinja2 HTML template (landing page)
├── static/
│   ├── img/            # App logo and demo screenshots
│   └── ...             # CSS / JS assets
└── venv/               # Local virtual environment (not committed)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sanket73/ai-sc-landing-page.git
cd ai-sc-landing-page

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the development server
python app.py
```

The app runs on **http://localhost:5002** by default.

---

## 🛠️ Tech Stack

### Landing Page
- **Flask** — lightweight Python web framework
- **Jinja2** — HTML templating
- **Vercel** — deployment and hosting

### SnapClass Core Application
- **Streamlit** — reactive frontend for the attendance app
- **FaceRecognition + Dlib** — facial biometric registration and matching (SFace)
- **Resemblyzer + Librosa** — voice embedding and speaker identification
- **Supabase** — PostgreSQL cloud database with real-time sync and auth

---

## 🔗 Deployment

The landing page is deployed on **Vercel** and live at:
👉 **[ai-sc-landing-page.vercel.app](https://ai-sc-landing-page.vercel.app)**

The main SnapClass application (Streamlit) is live at:
👉 **[ai-face-attendance-main.streamlit.app](https://ai-face-attendance-main.streamlit.app/)**

To deploy your own fork on Vercel, install the [Vercel CLI](https://vercel.com/docs/cli) and run:

```bash
vercel deploy
```

---

## 🗺️ Teacher Workflow

1. **Secure Login** — Encrypted authentication portal
2. **Interactive Dashboard** — Unified view of all subjects and rosters
3. **Course Management** — Create a subject and auto-generate everything needed
4. **FaceID Attendance** — Snap a photo; AI marks attendance in milliseconds
5. **Voice ID Attendance** — Sequential voice roll-call matched against stored embeddings
6. **Actionable Records** — Review logs, confidence scores, and download CSV reports

## 🎓 Student Workflow

1. **Instant Enrollment** — Join a course via QR code or course link
2. **Biometric Registration** — Register FaceID and VoiceID once; used for all future sessions
3. **Personal Dashboard** — Track attendance percentage across all subjects in real time

---

## 🤝 Contributing

Contributions are welcome! To get started:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
# Open a Pull Request on GitHub
```

Please keep PRs focused and include a clear description of what changed and why.

---

## 📄 License

This project is currently licensed. [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) 

---

## 👨‍💻 Author

**Sanket Dongardive**

[![GitHub](https://img.shields.io/badge/GitHub-Sanket73-181717?style=flat-square&logo=github)](https://github.com/Sanket73)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanket%20Dongardive-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sanket-dongardive-515793315)   

Built with ❤️ for educators everywhere.
