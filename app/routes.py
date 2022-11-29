
from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'Emanuel'}
    posts = [
            {
                'author': 'Juan',
                'body': 'Fuck You'

                },
            {
                'author': 'Jose',
                'body': 'Fucking retard'
                },
            ]
            
    return render_template('index.html', title='Welcome!', user=user,
            posts=posts)

