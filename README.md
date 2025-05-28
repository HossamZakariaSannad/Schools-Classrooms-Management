## 🌐 Live Demo

👉 [Click here to view the live app](https://schools-classrooms-management.onrender.com/)

# 🏫 Simple School Management System

This is a basic Django project for managing **schools** and **classes**. It is designed as a practice project to learn core Django concepts such as:

- Models (School, Class)
- Relationships between models (Class belongs to a School)
- Views, Templates, and Forms
- Basic CRUD operations (Create, Read, Delete)

---

## 💻 Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR-USERNAME/Schools-Classrooms-Management.git
    ```
2. Navigate into the project folder:
    ```bash
    cd Schools-Classrooms-Management
    ```
3. Create a virtual environment:
    ```bash
    python -m venv env
    ```
4. Activate the virtual environment:
    - On **Windows**:
        ```bash
        env\Scripts\activate
        ```
    - On **Linux/macOS**:
        ```bash
        source env/bin/activate
        ```
5. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```
8. Open your browser and visit:
    ```
    http://localhost:8000
    ```

---

## ⚙️ Technologies Used

- **Python 3.x** - Backend language
- **Django 4.x** - Web framework
- **SQLite** - Default development database
- **HTML & CSS** - For simple templates
- **Bootstrap** (optional) - For styling (if used)
- **VSCode** - Recommended editor

---

## 🚀 Project Functionalities

### 🏠 Home Page
- The **Home Page** acts as the main dashboard.
- It contains buttons that link to:
    - **School List Page**
    - **Class List Page**

---

### 🏫 School Management
- Add a **New School**, including:
    - School Name
    - School Area 
- View a **list of all schools**.
- Delete any school from the list.

---

### 🏛️ Class Management
- Each class is **linked to a specific school**.
- Add a **New Class**, including:
    - Class Name
    - Select the **School** it belongs to.
- View a **list of all classes**.
- Delete any class from the list.

---
