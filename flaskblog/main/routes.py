from flask import Blueprint, render_template, request

from flaskblog.main.forms import SearchForm
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(
        page=page, per_page=5
    )
    return render_template('home.html', posts=posts, title='Home')


@main.route('/about')
def about():
    return render_template('about.html', title='About')


@main.route('/search', methods=['GET', 'POST'])
def search():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('q') or request.form.get('ids')

    form = SearchForm()
    posts = None

    if search_query:
        posts = (
            Post.query.filter(Post.title.ilike(f'%{search_query}%'))
            .order_by(Post.date_posted.desc())
            .paginate(page=page, per_page=5)
        )

        if not form.ids.data:
            form.ids.data = search_query

    return render_template(
        'search.html', title='Search', form=form, posts=posts, q=search_query
    )
 