# Kavasam AI — Submission-Ready Full Product

**Your AI Companion for Safer Digital Life**

This is a complete, self-contained academic/demo product designed to be runnable locally today. It combines:

- React/Vite web application
- FastAPI REST backend
- SQLite persistence
- Registration/login with salted password hashing
- Hybrid phishing detector: rules + TF-IDF/Logistic Regression
- URL risk analysis
- Explainable WHAT / WHY / WHAT NOW output
- Detection history
- Cyber awareness score and recommendations
- Cyber Mentor
- Learning Center
- Scenario quiz and progress
- Local password-strength advisor (password text never sent to backend)
- Chromium Manifest V3 extension
- Simulated phishing demonstration page
- Health/API documentation

> **Important:** This is submission-ready for an academic demonstration and local deployment. A public production launch would still require professional security review, a larger validated dataset, HTTPS deployment, secret management, monitoring, rate limiting, privacy/legal review, and penetration testing.

## Requirements

- Windows 10/11
- Python 3.11+
- Node.js 20+
- Chrome or Edge
- VS Code recommended

## QUICK START — Windows

### Terminal 1 — Backend

```powershell
cd Kavasam-AI-Full\backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend: http://127.0.0.1:8000
API docs: http://127.0.0.1:8000/docs

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

### Terminal 2 — Frontend

```powershell
cd Kavasam-AI-Full\frontend
npm install
npm run dev
```

Open the Vite URL, normally http://localhost:5173

### Chrome extension

1. Open chrome://extensions
2. Enable Developer mode
3. Load unpacked
4. Select the `extension` folder
5. Pin Kavasam AI

### Demo page

Open `demo/phishing-demo.html` in Chrome. It is clearly labeled as a simulation.

## First-use flow

1. Register a new account.
2. Login.
3. Open Dashboard.
4. Use Is This Safe? with the sample phishing message.
5. Check the generated explanation and history.
6. Ask Cyber Mentor a question.
7. Complete a lesson/quiz.
8. Open Password Advisor and test a password locally.
9. Test the browser extension.

## Sample phishing text

URGENT! Your bank account will be blocked today. Verify your account immediately and send your OTP.

## Architecture

Browser/Extension → FastAPI → Authentication/SQLite → Hybrid Risk Engine → Explainability → History/Awareness → Learning/Quiz

## Security notes

- Passwords are hashed with PBKDF2-HMAC-SHA256 and random salts.
- Password advisor uses only local browser-side checks.
- Authentication tokens are short-lived signed JWTs.
- API input is validated with Pydantic.
- CORS is restricted to local development origins.
- Demo pages never request or transmit real credentials.

## Test commands

Backend:

```powershell
cd backend
.\venv\Scripts\Activate.ps1
pytest -q
```

Frontend build:

```powershell
cd frontend
npm run build
```

## 4-minute video script

**0:00–0:25** Problem + Kavasam introduction.

**0:25–0:55** Dashboard: awareness score, detections, learning progress.

**0:55–1:35** Is This Safe?: paste phishing message, show score and WHAT/WHY/WHAT NOW.

**1:35–2:00** History: show saved analysis.

**2:00–2:25** Cyber Mentor: ask “What is phishing?”

**2:25–2:45** Learning + Quiz: complete scenario.

**2:45–3:10** Password Advisor: demonstrate local strength feedback; explain password is not uploaded.

**3:10–3:45** Browser extension + simulated phishing page + right-click analysis.

**3:45–4:00** Close on: DETECT → EXPLAIN → EDUCATE → IMPROVE.

## What to say if asked “Is this really AI?”

“Kavasam uses a hybrid architecture. A transparent rule engine captures interpretable security indicators, while a lightweight TF-IDF plus Logistic Regression classifier adds a machine-learning signal. The final risk score combines those signals and generates an explanation. The architecture is intentionally lightweight for fast response and low-resource environments.”
