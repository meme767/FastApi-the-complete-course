# FastAPI: The Complete Course

Three projects I built while following the "FastAPI - The Complete Course 2026" course on Udemy. They progress from a basic REST API to a full application with a database, authentication and role-based authorization.

## Repository Structure

```
FastApi-the-complete-course/
├── books.py          # Project 1: basic Books API
├── books2.py         # Project 2: Books API with validation
└── Project 3/
    └── TodoApp/      # Project 3: Todo application with database and JWT auth
```

---

## Project 1: Books API (`books.py`)

A simple REST API that manages a list of books stored in memory. Each book has a title, author and category.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/mybook` | Static route example |
| GET | `/books/{book_title}` | Get a book by title (case-insensitive) |
| GET | `/books/{book_author}/?book_category=` | Filter books by author and category (query parameter) |
| POST | `/books/create_book/` | Add a new book (request body) |
| PUT | `/books/update_book` | Update a book by title |
| DELETE | `/books/delete_book/{book_title}` | Delete a book by title |

**Concepts:** HTTP methods (GET, POST, PUT, DELETE), path parameters, query parameters, request body, route ordering (static routes before dynamic ones).

---

## Project 2: Books API with Validation (`books2.py`)

An improved version of the Books API. Books are now objects with an id, title, author, description, rating and published date, and every request is validated with Pydantic.

- `Book` class for internal data and `BookRequest` (Pydantic model) for validating requests
- Field rules: title min 3 characters, description max 100 characters, rating from 1 to 5, published date from 1991 to 2026
- Auto-generated IDs for new books
- Path and query validation with `Path()` and `Query()`
- Proper status codes (200, 201, 204) and 404 errors with `HTTPException`
- Example request body shown in the Swagger docs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books` | Get all books |
| GET | `/books/{book_id}` | Get a book by ID |
| GET | `/books/?book_rating=` | Filter books by rating |
| GET | `/books/publish/?published_date=` | Filter books by published date |
| POST | `/create-book` | Create a book (201) |
| PUT | `/books/update_book` | Update a book (204) |
| DELETE | `/books/{book_id}` | Delete a book (204) |

**Concepts:** Pydantic models, `Field` validation, `Path` and `Query` validation, status codes, error handling.

---

## Project 3: TodoApp (`Project 3/TodoApp`)

A to-do application backend where each user manages their own todos. Data is stored in a relational database through SQLAlchemy (one user has many todos), and the API is secured with JWT authentication and role-based access (user and admin).

### Features
- User registration and login
- Password hashing with bcrypt
- JWT access tokens (OAuth2 password flow)
- Protected endpoints that require a valid token
- Full CRUD for todos, limited to the logged-in user's own todos
- Admin-only endpoints to view and delete any todo
- User endpoints to view the current user and change the password
- Database access through SQLAlchemy with dependency injection (`Depends`)
- Code split into routers: `auth`, `todos`, `admin`, `users`

### Project Structure

```
TodoApp/
├── main.py          # Application entry point, creates tables and includes routers
├── database.py      # Database engine, session and Base
├── models.py        # SQLAlchemy models (Users, Todos)
└── routers/
    ├── auth.py      # Registration, login, token creation
    ├── todos.py     # Todo CRUD for the current user
    ├── admin.py     # Admin-only operations
    └── users.py     # Current user info and password change
```

### Database Models

**Users:** id, email, username, first_name, last_name, hashed_password, is_active, role

**Todos:** id, title, description, priority, complete, owner_id (foreign key to Users)

### Main Endpoints

| Router | Method | Endpoint | Description |
|--------|--------|----------|-------------|
| Auth | POST | `/auth/` | Register a new user |
| Auth | POST | `/auth/token` | Log in and get an access token |
| Todos | GET | `/` | Get all todos of the current user |
| Todos | GET | `/todo/{todo_id}` | Get one todo |
| Todos | POST | `/todo` | Create a todo |
| Todos | PUT | `/todo/{todo_id}` | Update a todo |
| Todos | DELETE | `/todo/{todo_id}` | Delete a todo |
| Admin | GET | `/admin/todo` | Get all todos (admin only) |
| Admin | DELETE | `/admin/todo/{todo_id}` | Delete any todo (admin only) |
| Users | GET | `/user` | Get current user info |
| Users | PUT | `/user/password` | Change password |

Protected endpoints require the header `Authorization: Bearer <token>`.

**Concepts:** SQLAlchemy ORM, JWT authentication, password hashing, authorization with roles, dependency injection, routers.

---

## Tech Stack
Python, FastAPI, Pydantic, SQLAlchemy, JWT (python-jose), passlib/bcrypt, Uvicorn

## How to Run

```bash
git clone https://github.com/meme767/FastApi-the-complete-course.git
cd FastApi-the-complete-course

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy pydantic python-jose passlib bcrypt python-multipart

# Projects 1 and 2
uvicorn books:app --reload
uvicorn books2:app --reload

# Project 3
cd "Project 3/TodoApp"
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

### Using the TodoApp API
1. Register a user with `POST /auth/`
2. Log in with `POST /auth/token` to get an access token
3. Click **Authorize** in Swagger UI (or send the `Authorization: Bearer <token>` header)
4. Create and manage your todos

## What I Learned
- Building REST APIs with FastAPI
- Validating data with Pydantic
- Working with a database using SQLAlchemy
- Securing endpoints with JWT and role-based authorization
- Organizing a backend project into routers and modules

