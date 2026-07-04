# 🇮🇳 Government Scheme Advisor Chatbot

An AI-powered **Government Scheme Recommendation System** built with **Streamlit** and the **Hugging Face Inference API**. The application helps users discover relevant **Central and State Government Schemes** based on their profile, including age, occupation, income, state, gender, and category.

The chatbot provides personalized recommendations, explains eligibility, and answers follow-up questions through a clean and interactive conversational interface.

---

## ✨ Features

- 🎯 Personalized government scheme recommendations
- 🤖 AI-powered chatbot using Hugging Face Inference API
- 📋 User profile-based eligibility analysis
- 💬 Interactive follow-up conversation
- 🌙 Modern dark-themed responsive UI
- 📝 Session-based chat history
- 🗂️ Sidebar profile form for quick inputs
- 🗑️ One-click chat history clearing
- 🇮🇳 Focused exclusively on Indian Government Schemes
- ⚡ Fast and lightweight Streamlit application

---

# 📸 Demo

> Add screenshots after deployment.

### Home Page

![Home](assets/home.png)

### Recommendation Result

![Recommendation](assets/recommendation.png)

### Chat Interface

![Chat](assets/chat.png)

---

# 🛠️ Tech Stack

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### AI Models
- Qwen2.5-7B-Instruct
- DeepSeek-V3-0324

### API
- Hugging Face Inference API

### Libraries
- Streamlit
- Hugging Face Hub
- Python Dotenv
- Requests
- Transformers
- Torch
- SentencePiece
- tqdm

---

# 📂 Project Structure

```
Government-Scheme-Advisor/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
├── assets/
│   ├── home.png
│   ├── recommendation.png
│   └── chat.png
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/satya-anand-ml/Government-Scheme-Advisor.git
```

```bash
cd Government-Scheme-Advisor
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create a `.env` File

Create a `.env` file in the project root directory.

```env
HF_TOKEN=your_huggingface_access_token
```

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

The application will automatically open in your browser.

---

# 📋 User Inputs

The chatbot collects the following details:

- Age
- Gender
- Occupation
- Monthly Income
- State
- Category

These details are used to generate personalized government scheme recommendations.

---

# 🧠 How It Works

### Step 1

The user enters personal information through the sidebar.

↓

### Step 2

The application creates a structured prompt using the entered details.

↓

### Step 3

The prompt is sent to the Hugging Face Inference API.

↓

### Step 4

The AI model analyzes the user's eligibility.

↓

### Step 5

The chatbot recommends:

- Suitable Central Government Schemes
- Suitable State Government Schemes
- Eligibility Criteria
- Benefits
- Application Process

↓

### Step 6

Users can continue asking follow-up questions through the chat interface.

---

# 🤖 AI Prompt Rules

The chatbot is instructed to:

- Recommend only REAL Indian Government Schemes
- Prefer State schemes before Central schemes
- Clearly explain eligibility
- Clearly mention ineligibility when applicable
- Provide simple application steps
- Respond in plain English
- Refuse unrelated questions politely
- Redirect users to scheme-related queries

---

# 📦 Requirements

```
python-dotenv==1.0.1
streamlit==1.32.2
torch>=2.10.0
transformers>=4.36.0
sentencepiece>=0.1.99
requests==2.31.0
tqdm==4.66.1
```

---

# 🔒 Environment Variables

This project requires a Hugging Face API token.

```
HF_TOKEN=your_token_here
```

> **Note:** Never upload your `.env` file to GitHub.

---

# 🚀 Future Enhancements

- 🌐 Multilingual Support
- 🎙️ Voice Assistant
- 📄 PDF Report Generation
- 📍 Automatic Location Detection
- 🔍 Smart Scheme Search
- ❤️ Save Favorite Schemes
- 📊 Better Eligibility Analysis
- 🏛️ Government API Integration
- 🔔 Scheme Update Notifications
- 📱 Mobile Responsive Improvements

---

# ⚠️ Disclaimer

This chatbot provides AI-assisted recommendations based on the information entered by the user.

Government schemes, eligibility criteria, and application processes may change over time.

Users are advised to verify all information from the official Government of India and respective State Government portals before applying.

---

# 👨‍💻 Author

**Satya Anand**

B.Tech CSE Student  
Haldia Institute of Technology

### GitHub

https://github.com/satya-anand-ml

### LinkedIn

https://www.linkedin.com/in/your-linkedin-profile

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

## 🇮🇳 Built with ❤️ to help citizens discover the right Government Schemes.