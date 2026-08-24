# Daily Tasks Tracker - Backend

A Django REST API for managing daily tasks with JWT authentication. Built as a training project for time management.

## Tech Stack

- Backend: Django 5.1 + Django REST Framework
- Authentication: JWT (SimpleJWT)
- Database: SQLite (development) / PostgreSQL (production)
- API Documentation: Swagger/OpenAPI (drf-spectacular)

## Features

- User Registration and Login (email/password)
- JWT Authentication (access + refresh tokens)
- Task CRUD operations
- Task completion tracking
- Date-based task filtering
- Priority levels (LOW, MEDIUM, HIGH)
- Admin panel
- API documentation (Swagger UI)

## Project Structure
```
Daily Tasks/
├── Backend/
│ ├── daily_tasks_backend/ # Django project settings
│ ├── users/ # Custom user model & auth
│ ├── tasks/ # Task management
│ ├── manage.py
│ ├── requirements.txt
│ └── .env # Environment variables
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.12+
- pip

### Installation

1. Clone the repository:
```
git clone https://github.com/jona339e/daily-tasks-backend.git
cd daily-tasks-backend/Backend
```

2. Create and activate virtual environment:
windows
```
python -m venv venv
venv\Scripts\activate
```
macOS/Linux
```
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```pip install -r requirements.txt```

4. Create .env file:
```cp .env.example .env```

5. Run migrations:

```python manage.py migrate```

6. Create superuser:

```python manage.py runserver```


8. Access the application:
- API: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin
- API Documentation: http://127.0.0.1:8000/api/docs

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register new user |
| POST | /api/auth/login | Login with email/password |
| POST | /api/auth/logout | Logout (blacklist token) |
| GET | /api/auth/me | Get current user profile |

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/tasks/ | Get tasks (filter by date) |
| POST | /api/tasks/ | Create new task |
| GET | /api/tasks/{id}/ | Get single task |
| PUT | /api/tasks/{id}/ | Update task (full) |
| PATCH | /api/tasks/{id}/ | Update task (partial) |
| DELETE | /api/tasks/{id}/ | Delete task |
| PATCH | /api/tasks/{id}/complete | Toggle completion status |

## Environment Variables

Create a .env file in the Backend directory:
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3


## Database Schema

### Users Table
- id (UUID, primary key)
- email (unique)
- display_name
- avatar_url
- google_id
- created_at
- is_active
- is_staff

### Tasks Table
- id (UUID, primary key)
- user (foreign key to Users)
- title
- description
- due_date
- start_time
- estimated_duration_minutes
- actual_duration_minutes
- is_completed
- completed_at
- priority (LOW, MEDIUM, HIGH)
- created_at
- updated_at

## Testing
```python manage.py test```

## Future Enhancements

- Google OAuth login
- Rate limiting
- Offline sync endpoint
- Push notifications
- Task recurrence
- Gamification (XP, achievements, streaks)

## License

MIT License - see LICENSE file for details.

## Author

Jonas - GitHub: jona339e