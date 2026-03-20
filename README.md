# Flask Blog Application

This is a simple blog web application built with Flask. Users can register, log in, update their profile, and create posts.

## Core Features

- **Registration and Authentication**: Users can create accounts and log in securely.
- **User Profiles**: Ability to update username, email, and upload an avatar.
- **Post Management**: Create and view blog entries.
- **Database**: Uses SQLite with SQLAlchemy ORM.

## Installation and Setup

### 1. Environment Setup
Make sure you have Python installed. It is recommended to use a virtual environment:

```bash
# Create a virtual environment
python -m venv .venv

# Activation (Linux/macOS)
source .venv/bin/activate

# Activation (Windows)
.venv\Scripts\activate
```

### 2. Install Dependencies
Install the required packages (if they are not already installed):

```bash
pip install flask flask-sqlalchemy flask-bcrypt flask-login flask-wtf email-validator pillow python-dotenv
```

### 3. Configuration
The secret key (`SECRET_KEY`) is stored in a separate `.env` file for security. Ensure that the `.env` file contains the key:

```env
SECRET_KEY=your_secret_key
```

### 4. Run the Application
You can run the application via the `run.py` file:

```bash
python run.py
```

After that, the application will be available at: `http://127.0.0.1:5000`

## Project Structure

- `flaskblog/`: Main application package.
  - `models.py`: Database models (User, Post).
  - `routes.py`: Application routes and logic.
  - `forms.py`: Registration, login, and post creation forms.
  - `static/`: Static files (CSS, profile pictures).
  - `templates/`: HTML templates.
- `run.py`: Entry point to start the server.
- `.env`: File with secret environment variables.
- `site.db`: SQLite database (created automatically).
