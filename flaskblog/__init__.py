from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy

from flaskblog.config import Config

load_dotenv()


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

page_down = PageDown()


def render_markdown(text):
    import markdown

    return markdown.markdown(text, extensions=['extra', 'codehilite'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    page_down.init_app(app)

    app.add_template_filter(render_markdown, 'markdown')

    from flaskblog.errors.handlers import errors
    from flaskblog.main.routes import main
    from flaskblog.posts.routes import posts
    from flaskblog.users.routes import users

    app.register_blueprint(errors)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
