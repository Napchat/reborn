from app import application

'''decorators which associate the URLs / and /index to this function
This means that when a web browser requests either of these two URLs, 
Flask is going to invoke this function and pass its return value back to the browser as a response
'''
@application.route('/')
@application.route('/index')
def index():
    return "Hello,World!"