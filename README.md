# Employee Management API

A simple REST API built using FastAPI for managing employee records.

## Features

- Add Employee
- Get All Employees
- Get Employee by ID
- Update Employee
- Delete Employee

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```
employee_api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── storage.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to the project

```bash
cd employee_api
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open Swagger

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /employees | Create Employee |
| GET | /employees | Get All Employees |
| GET | /employees/{id} | Get Employee |
| PUT | /employees/{id} | Update Employee |
| DELETE | /employees/{id} | Delete Employee |

## Future Improvements

- PostgreSQL Integration
- SQLAlchemy ORM
- JWT Authentication
- Docker
- Unit Testing

## Author

Shikhar Saxena