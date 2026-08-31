# 🛡️ KAVASAM AI

### AI-Powered Cybersecurity Awareness Browser Extension

> **Detect. Understand. Act Safely.**

Kavasam AI is an AI-powered cybersecurity awareness platform designed to help everyday users identify, understand, and respond to online cyber threats.

The **browser extension is the core product**. It brings cybersecurity assistance directly into the user's browsing experience, allowing suspicious content to be analyzed without requiring the user to leave the webpage.

---

## 🚨 Problem

As digital usage increases, users are constantly exposed to phishing messages, suspicious links, fake websites, malicious content, and other cyber threats.

The major problem is not only detecting these threats — it is helping ordinary users **understand what is dangerous and what they should do next**.

Many existing cybersecurity tools provide technical warnings that can be difficult for beginners to understand.

---

## 💡 Solution

Kavasam AI acts as an intelligent cybersecurity assistant inside the browser.

When a user encounters suspicious content, they can use the Kavasam AI extension to analyze it.

### Core workflow

```text
Suspicious Content
        ↓
Kavasam AI Browser Extension
        ↓
AI-Powered Analysis
        ↓
Risk Identification
        ↓
Simple Explanation
        ↓
Recommended Action
```

Instead of simply saying **"Dangerous"**, Kavasam AI helps the user understand:

* What the potential threat is
* Why it may be dangerous
* How serious the risk is
* What action the user should take

---

# ✨ Key Features

### 🛡️ AI Cybersecurity Analyzer

Analyze suspicious messages, links, and online content.

### ⚠️ Risk Detection

Identify potentially unsafe or suspicious content and communicate the risk clearly.

### 💡 Simple Threat Explanation

Convert complex cybersecurity analysis into understandable guidance for non-technical users.

### ✅ Recommended Action

Provide practical next steps so users can make safer decisions.

### 🔐 Password Security Guidance

Help users understand password strength and improve their security practices.

### 🤖 Cybersecurity Assistant

Provide beginner-friendly cybersecurity guidance through an AI-powered conversational interface.

---

# 🧩 Browser Extension

The **Kavasam AI browser extension is the primary interface of the project.**

It is designed to work directly where users encounter online threats.

### Extension Flow

```text
User encounters suspicious content
                ↓
       Opens Kavasam AI
                ↓
          Content is analyzed
                ↓
       AI identifies the risk
                ↓
      Risk + explanation shown
                ↓
       Safer action suggested
```

---

# 🎥 Demo


# 🏗️ System Architecture

```text
                    USER
                      │
                      ▼
          ┌─────────────────────┐
          │ Kavasam AI Browser  │
          │      Extension      │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Input / Content /   │
          │ URL Analysis        │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ AI Analysis Engine  │
          └──────────┬──────────┘
                     │
              ┌──────┴──────┐
              ▼             ▼
       Threat Analysis   Risk Score
              │             │
              └──────┬──────┘
                     ▼
          ┌─────────────────────┐
          │ Simple Explanation  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Recommended Action  │
          └─────────────────────┘
```

---

# 💻 Technology Stack

### Browser Extension

* HTML
* CSS
* JavaScript
* Chrome Extension APIs

### Backend

* Python
* FastAPI

### AI

* AI/NLP-based analysis
* Cybersecurity risk assessment
* Threat classification and explanation

### Development

* IBM Bob
* GitHub
* VS Code / Development tools

---

# 🤖 IBM Bob

IBM Bob was used as an **AI-assisted development partner** during the development of Kavasam AI.

It supported activities including:

* Project architecture and planning
* Browser extension development
* Frontend implementation
* Backend/API development
* Debugging
* Error analysis
* Code refinement
* Integration between components
* Documentation

The development process was iterative:

```text
Idea
 ↓
Architecture
 ↓
AI-Assisted Development with IBM Bob
 ↓
Implementation
 ↓
Testing
 ↓
Debugging
 ↓
Refinement
 ↓
Working Prototype
```



# 📁 Repository Structure

```text
KAVASAM-AI/
│
├── extension/              # Core browser extension
├── backend/                # Backend/API services
├── web/                    # Web platform
│
├── demo/
│   └── screenshots/        # Product screenshots
│
├── README.md
├── IBM_BOB_USAGE.md        # IBM Bob usage documentation
├── requirements.txt
└── .gitignore
```

---

# 🚀 Running the Project

## 1. Clone the repository

```bash
git clone https://github.com/kethsi-giftlinsvg/KAVASAM-AI.git
cd KAVASAM-AI
```

## 2. Run the backend

```bash
cd backend
```

Create and activate a Python virtual environment, then install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn main:app --reload
```

## 3. Load the browser extension

1. Open Google Chrome.
2. Go to:

```text
chrome://extensions/
```

3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select the `extension` folder.
6. Pin **Kavasam AI** to the Chrome toolbar.
7. Click the extension icon to use it.

> Configuration requirements may vary depending on the final implementation.

---

# 🎯 Impact

Kavasam AI is designed to make cybersecurity more accessible to everyday users.

The goal is to move cybersecurity from:

**Complex warnings → Simple understanding → Safer decisions**

By providing assistance directly inside the browser, Kavasam AI can help users recognize threats at the moment they encounter them.

---

# 🔮 Future Scope

Future versions can expand Kavasam AI with:

* Real-time phishing detection
* Malicious URL intelligence
* Website trust scoring
* Multilingual cybersecurity explanations
* Personalized security recommendations
* Expanded threat intelligence integration
* Enterprise security awareness features

---

# 👥 Team

### Kavasam AI

**IBM SkillsBuild Hackathon 2026**

**Domain:** Artificial Intelligence + Cybersecurity

---

## 🛡️ Our Vision

> **Don't just detect the threat. Help the user understand it.**
