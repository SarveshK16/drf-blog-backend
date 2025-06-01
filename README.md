# DRF Blog Backend

**DRF Blog Backend** is a Django REST Framework–powered API that provides endpoints for managing blog posts. It allows users to create, read, update, and delete blog entries through a RESTful interface.

---

## 🚀 Features

- 📝 Blog Post CRUD operations (Create, Read, Update, Delete)
- 🔐 Secure and JWT authenticated API endpoints
- 📦 JSON-based API responses for easy frontend integration

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment tool (optional but recommended)

---

1. **Clone the repo**

```bash
git clone https://github.com/SarveshK16/drf-blog-backend.git
cd new_django_api
```
2. **Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt
```
4. **Apply migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Run the development server:**

```bash
python manage.py runserver
```
6. **Access the application:** Open your browser and navigate to http://localhost:8000/

---

## 📁 Project Structure

```bash
new_django_api/
├── new_django_api/     # Main Django Project
├── media/              # Store media files, user uploaded images
├── blogapp/            # Django app for blog functionalities
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies 
└── .gitignore          # Git ignore file
```

---

## 📄 License
This project is licensed under the MIT License.

---

## 📬 Contact
For any inquiries or feedback, please reach out to sskulkarni161@gmail.com
