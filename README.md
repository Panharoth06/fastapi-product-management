# 🛍️ Product Management Service

A **FastAPI-based microservice** for managing product data — built for speed, scalability, and clean API design.

---

## 🚀 Features

- 🔧 Full CRUD operations for products
- 🌐 RESTful API endpoints
- 📄 Interactive API docs via Swagger (`/docs`) and ReDoc (`/redoc`)
- 🧩 Easy integration with other services

---

## ⚙️ Setup

### 1️⃣ Create a Virtual Environment

It’s recommended to use a virtual environment to isolate dependencies.

```bash
python -m venv venv
```

Then activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows (PowerShell)**

```bash
venv\Scripts\activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Service

Start the FastAPI server with **Uvicorn**:

```bash
uvicorn main:app --reload
```

---

## 📚 API Documentation

Once the server is running, you can access:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc UI:** http://localhost:8000/redoc

---

## 🧠 Notes

- Default port is `8000`. You can change it using:
    
    ```bash
    uvicorn main:app --reload --port 8080
    ```
    
- Make sure your `.env` or configuration file (if any) is properly set before running in production.

---

## 🧩 Tech Stack

- **FastAPI** — high-performance Python web framework
- **Uvicorn** — lightning-fast ASGI server
- **Pydantic** — for data validation and serialization