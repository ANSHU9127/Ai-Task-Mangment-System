# AI Task & Knowledge Management System

## Overview
This project is an AI-based system where admins upload documents and users can search information and complete tasks.

## Features
- JWT Authentication (login system)
- Role-based access (admin and user)
- Document upload
- AI semantic search using FAISS
- Task management (create, update)
- Task filtering (status-based)
- Basic analytics

## Tech Stack
- FastAPI (Backend)
- MySQL (Database)
- FAISS + Sentence Transformers (AI search)
- SQLAlchemy

## How it works
1. Admin uploads documents  
2. Documents are converted into embeddings  
3. User searches query  
4. System finds similar results using AI  
5. Tasks are created and managed  

## Run Project
cd backend  
source venv/bin/activate  
python3 -m uvicorn main:app --reload  

Open: http://127.0.0.1:8000 

## Author
Anshu Kumar Roy
