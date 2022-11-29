
from flask import render_template
from app import flask_app

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username': 'Emanuel'}
    posts = [
            {
                'author': {'username': 'Juan'},
                'body': 'It\'s bloody hot today'

                },
            {
                'author': {'username': 'Jose'},
                'body': 'The Government sucks'
                },
            ]
            
    return render_template('index.html', title='Welcome!', user=user,
            posts=posts)

