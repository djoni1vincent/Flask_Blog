# Flask-Blog Application

A feature-rich, full-stack blog application built with Python and the Flask web framework. This project follows modern web development patterns, including modular architecture with Blueprints and secure database interactions with SQLAlchemy.

## 🚀 Live Demo
The application is deployed and available at:
[http://13.62.18.132/home](http://13.62.18.132/home)

## ✨ Key Features
- **User Authentication:** Secure registration, login, and logout functionality using Flask-Login and Bcrypt for password hashing.
- **Post Management:** Fully functional CRUD (Create, Read, Update, Delete) operations for blog posts.
- **User Profiles:** Personalized user accounts with the ability to update account details (username, email) and upload custom profile pictures.
- **Markdown Support:** Write and render blog posts using Markdown syntax with live preview (via Flask-PageDown).
- **Search Functionality:** Integrated search feature to quickly find posts by title.
- **Pagination:** Clean and efficient post navigation on the home and search pages.
- **Password Reset:** Secure password recovery system using email-based tokens.
- **Responsive Design:** A modern, not 'mobile-friendly' interface built with Bootstrap 5 and custom CSS.
- **Custom Error Handling:** Dedicated pages for common HTTP errors (403, 404, 500).

## 🛠️ Tech Stack
- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **Database:** [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
- **Forms:** [Flask-WTF](https://flask-wtf.readthedocs.io/)
- **Security:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/)
- **Authentication:** [Flask-Login](https://flask-login.readthedocs.io/)
- **Mail:** [Flask-Mail](https://pythonhosted.org/flask-mail/)
- **Markdown:** [Flask-PageDown](https://pythonhosted.org/Flask-PageDown/) & [Markdown](https://pythonhosted.org/Markdown/)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Image Processing:** [Pillow](https://python-pillow.org/)

## 📂 Project Structure
The application follows the "Application Factory" pattern with modular blueprints:
- `flaskblog/users`: User-related routes (auth, account, profile pics).
- `flaskblog/posts`: Blog post management (CRUD).
- `flaskblog/main`: Core pages (Home, About, Search).
- `flaskblog/errors`: Custom error handlers.
- `flaskblog/models.py`: Database schema and relationships.
- `flaskblog/static`: CSS, JS, and user-uploaded media.
- `flaskblog/templates`: Jinja2 templates for all views.

---
*Note: This project was developed as part of a Python/Flask learning path, focusing on scalable architecture and secure web development practices.*
