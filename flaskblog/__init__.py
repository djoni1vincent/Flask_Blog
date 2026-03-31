import markdown
from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy

load_dotenv()


app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail(app)

page_down = PageDown(app)


@app.template_filter('markdown')
def render_markdown(text):
    return markdown.markdown(text, extensions=['extra', 'codehilite'])


from flaskblog.main.routes import main
from flaskblog.posts.routes import posts
from flaskblog.users.routes import users

app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(users)
