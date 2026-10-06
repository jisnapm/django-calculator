# Django Calculator API

A REST-style calculator API built with **Django** and **Django REST Framework concepts**, created as a learning project to practice handling JSON requests, API endpoints, Django views, and basic backend logic.

## Features

The API provides endpoints for various mathematical and utility operations:

- Addition
- Subtraction
- Multiplication
- Division
- Factorial
- Prime Number Check
- Palindrome Check
- Armstrong Number Check
- Age Calculation
- BMI Calculation
- Electricity Bill Calculation

## 🛠️ Technologies Used

- **Python**
- **Django**
- **JSON**
- **REST API concepts**
- **SQLite**
- **Git & GitHub**
- **VS Code**

## Project Structure

```text
django-calculator/
│
├── calculatorApp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── django_calculator/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── APIDOC.http
├── manage.py
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jisnapm/django-calculator.git
```

### 2. Navigate to the project

```bash
cd django-calculator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/add/` | POST | Adds two numbers |
| `/subtract/` | POST | Subtracts two numbers |
| `/multiply/` | POST | Multiplies two numbers |
| `/divide/` | POST | Divides two numbers |
| `/factorial/` | POST | Calculates factorial |
| `/prime/` | POST | Checks whether a number is prime |
| `/palindrome/` | POST | Checks whether a number/string is palindrome |
| `/armstrong/` | POST | Checks whether a number is Armstrong |
| `/age/` | POST | Calculates age |
| `/bmi/` | POST | Calculates BMI |
| `/electricity/` | POST | Calculates electricity bill |

> The exact request fields and responses can be found in `APIDOC.http`.

## Testing the API

You can test the endpoints using:

- VS Code REST Client
- Postman
- Thunder Client
- Any API testing tool

Example request:

```http
POST http://127.0.0.1:8000/add/
Content-Type: application/json

{
    "num1": 10,
    "num2": 20
}
```

Example response:

```json
{
    "Sum": 30
}
```

## What I Learned

Through this project, I practiced:

- Django project and app structure
- Django URL routing
- Function-based and class-based views
- Handling HTTP POST requests
- Reading JSON request bodies
- Converting JSON data into Python dictionaries
- Returning JSON responses
- Working with Django models
- Database migrations
- Building API endpoints
- Testing APIs using REST Client
- Using Git and GitHub for version control

## Future Improvements

Some possible improvements for this project:

- Add proper input validation
- Add error handling
- Add automated unit tests
- Use Django REST Framework serializers
- Add API documentation with Swagger/OpenAPI
- Improve response formats and HTTP status codes
- Add a frontend interface

## Author

**Jisna P M**

GitHub: [@jisnapm](https://github.com/jisnapm)

---

⭐ If you find this project useful, feel free to star the repository!