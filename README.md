# Text Extract & Summarize

Text Extract & Summarize is a lightweight SaaS application that extracts text from URLs or uploaded files and generates concise summaries using OpenAI's GPT model.

## 🚀 Features (MVP Scope)

- ✅ Extract text from a publicly accessible URL
- ✅ Generate a summary using OpenAI
- ✅ REST API for URL-based summarization
- 🟡 File upload support (PDF, TXT, DOCX) *(in progress)*
- 🟡 Store extracted + summarized content in database
- 🟡 CRUD API for managing summaries
- ⬜ Simple frontend UI (React/Vite)
- ⬜ Secure and rate-limited endpoints
- ⬜ Containerized deployment (Docker)

## 🛠️ Tech Stack

- **Backend**: Python, Django, Django REST Framework
- **AI Summarization**: OpenAI GPT API
- **Containerization**: Docker, docker-compose
- **Environment Management**: `.env` file for secrets
- **Planned**: AWS (S3, EC2), Terraform

## 📦 Project Structure

