from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Bouette'} # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Bagel'}, 
            'body': 'Beautiful day in Sainte-Cecile!' 
        },
        { 
            'author': {'nickname': 'Kak'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
