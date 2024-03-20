from flask import render_template
from app import application

'''decorators which associate the URLs / and /index to this function
This means that when a web browser requests either of these two URLs, 
Flask is going to invoke this function and pass its return value back to the browser as a response
'''
@application.route('/')
@application.route('/index')
def index():
    user = {'username':'shangnan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)