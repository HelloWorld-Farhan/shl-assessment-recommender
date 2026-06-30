# 🤖 SHL Conversational Assessment Recommender API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini_AI-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white"/>
  <img src="https://img.shields.io/badge/FAISS-1C1C1C?style=for-the-badge&logo=meta&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge"/>
</p>

<p align="center">
  A <strong>Conversational AI Recommender System</strong> built for recruiters and hiring managers. Powered by <strong>Google Gemini</strong> and <strong>Retrieval-Augmented Generation (RAG)</strong> using FAISS, this API seamlessly translates vague user queries into highly accurate, real-world assessment recommendations from the SHL product catalog.
</p>

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 **Conversational AI** | Uses Google Gemini to understand complex natural language queries |
| 🔍 **RAG System** | FAISS vector database ensures recommendations are grounded in reality |
| 🛡️ **Hallucination Prevention** | Strictly refuses to recommend tests outside the official catalog |
| 💬 **Clarifying Questions** | AI intelligently asks follow-up questions for vague requests |
| ⚡ **FastAPI Backend** | High-performance, asynchronous REST API architecture |
| 🐳 **Docker Ready** | Fully containerized for instant deployment to cloud platforms |

---

## 📂 Project File Structure

```
shl-assessment-recommender/
│
├── main.py                    ← FastAPI application & endpoints
├── agent.py                   ← Gemini LLM logic & prompt engineering
├── retriever.py               ← FAISS vector database setup & BM25 logic
├── models.py                  ← Pydantic schemas for data validation
├── evaluate.py                ← Automated testing & evaluation script
├── debug.py                   ← Interactive terminal debugger
│
├── shl_product_catalog.json   ← SHL Assessment JSON Dataset
├── requirements.txt           ← Python dependencies
├── Dockerfile                 ← Hugging Face & Docker deployment script
├── render.yaml                ← Render.com deployment blueprint
└── .env                       ← Environment variables (API Keys)
```

---

## ⚙️ Prerequisites

Before you begin, make sure you have the following:

- ✅ **Python 3.10+** — installed on your local machine
- ✅ **Google Gemini API Key** — available for free from Google AI Studio
- ✅ **Git** — for cloning the repository

---

## 🚀 Step-by-Step Setup Guide

### Step 1 — Clone the Repository

Open a terminal or Git Bash and run:

```bash
git clone https://github.com/HelloWorld-Farhan/shl-assessment-recommender.git
cd shl-assessment-recommender
```

---

### Step 2 — Create Environment Variables

Create a file named `.env` in the root folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

---

### Step 3 — Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

### Step 4 — Run the API Locally

Start the Uvicorn server:

```bash
uvicorn main:app --reload
```

Your API is now running at: `http://127.0.0.1:8000`

---

## ☁️ Deployment

### Option 1: Hugging Face Spaces (Recommended)
1. Create a new **Docker** Space on Hugging Face.
2. Upload all project files via the browser.
3. Add your `GEMINI_API_KEY` to the Space Secrets.
4. Hugging Face will automatically build and host the API using the provided `Dockerfile`.

### Option 2: Render.com
1. Connect your GitHub repository to Render.
2. Use the **Blueprint** option to automatically detect the `render.yaml` file.
3. Add your `GEMINI_API_KEY` to the Environment Variables.

---

## 🛠️ API Endpoints

### `GET /health`
Returns the status of the server.
**Response:** `{"status": "ok"}`

### `POST /chat`
Conversational endpoint for the recommender bot.
**Request Body:**
```json
{
  "user_message": "I need a test for a Java Developer",
  "history": []
}
```
**Response:**
```json
{
  "reply": "I found several Java assessments...",
  "recommendations": [
    {
      "name": "Core Java (Advanced Level)",
      "url": "https://www.shl.com/...",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

---

## 👨💻 Author

**Farhan Khalid** — Android & ML Engineer | Web Developer  
📧 farhankhalid17968@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/farhan-khalid-117514259/)  
🐙 [GitHub](https://github.com/HelloWorld-Farhan)  
🌐 [Portfolio](https://farhan-khalid-portfolio.vercel.app)

---

## 📄 License

```
MIT License

Copyright (c) 2026 Farhan Khalid

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🌟 Star This Repo

If you found this project helpful or interesting, please consider giving it a ⭐ on GitHub!

---

<p align="center">Made with ❤️ in India</p>
