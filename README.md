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

```
textextract/
├── api/                  # Django app for API logic
│   ├── views.py          # API endpoints
│   ├── serializers.py    # DRF serializers (planned)
│   ├── models.py         # DB models (planned)
├── openai_api.py         # GPT summarization logic
├── extract_text.py       # Text extraction from URLs
├── docker-compose.yml    # Container orchestration
├── Dockerfile            # Image config
├── .env                  # API keys and secrets
└── manage.py
```

## 🔧 Setup Instructions (Local Dev)

```bash
# Clone the repo
git clone https://github.com/markiskorova/textextract.git
cd textextract

# Copy and edit your OpenAI key
cp .env.example .env
# Add OPENAI_API_KEY=your-key

# Run with Docker
docker-compose up --build
```

## 📬 API Endpoints (Current)

| Method | Endpoint         | Description                    |
|--------|------------------|--------------------------------|
| POST   | `/api/extract/`  | Submit a URL to summarize      |
| POST   | `/api/upload/`   | Upload file to summarize *(todo)* |
| GET    | `/api/texts/`    | List all summaries *(todo)*    |
| GET    | `/api/texts/<id>/`| Get one summary *(todo)*      |
| DELETE | `/api/texts/<id>/`| Delete a summary *(todo)*     |

## 📌 Roadmap

- [ ] Add file upload handling
- [ ] Build CRUD API endpoints
- [ ] Add simple frontend
- [ ] Integrate AWS S3 for file storage
- [ ] Deploy with Terraform and AWS EC2

## 📄 License

MIT License. See `LICENSE` file.

---

### 👤 Author

Built by [@markiskorova](https://github.com/markiskorova) – Contributions welcome!
