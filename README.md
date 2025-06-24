# FastAPI Auto-Suggest API

This project provides a simple **Auto-Suggest API** built with **FastAPI**, which maps user input (like `banana`) to a predefined category (like `fruit`).

---

##  Features

- RESTful API with FastAPI
- Auto-maps item to a category
- Returns friendly messages like `Banana is a fruit`
- Supports CORS for frontend integration
- Dockerized for easy deployment

---

##  Requirements

You must have one of the following setups:

### Option 1: Run via Docker (Recommended)

- Docker installed
- type "**make build**" command to build the image
- just type "**make start**" command to start docker 
- 
### Option 2: Run Locally (Development)
- Python 3.12+
- Poetry (for dependency management)
- type "poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000"






