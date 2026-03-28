# 🚀 AI Task & Knowledge Management System

## 📌 Overview

This project is an AI-based system where admins upload documents and users can search information and complete tasks.

---

## ⚙️ Features

* JWT Authentication (login system)
* Role-based access (Admin/User)
* Document upload (.txt files)
* AI semantic search using FAISS
* Task management (create, update)
* Task filtering (status-based)
* Basic analytics

---

## 🛠️ Tech Stack

* Backend: FastAPI (Python)
* Database: MySQL
* AI: Sentence Transformers + FAISS
* ORM: SQLAlchemy
* Frontend: React.js

---

## 🚀 How to Run

### 🔹 Backend

cd backend
source venv/bin/activate
python3 -m uvicorn main:app --reload

Open: http://127.0.0.1:8000

---

### 🔹 Frontend

cd frontend
npm install
npm start

Open: http://localhost:3000

---

## 🔄 API Flow

1. Login → `/auth/login`
2. Upload document → `/documents`
3. Search → `/search?q=...`
4. Create task → `/tasks`
5. Filter tasks → `/tasks?status=pending`
6. View analytics → `/analytics`

---

## 🧠 How it works

* Documents are uploaded and split into chunks
* Each chunk is converted into embeddings
* Embeddings are stored in FAISS
* User query is also converted into embedding
* Similar results are retrieved using vector search

---

## 📌 Note

* Backend must be running for frontend to work
* Upload document before searching

---

## 👨‍💻 Author

Anshu Kumar Roy
