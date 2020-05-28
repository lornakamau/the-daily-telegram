from flask import render_template #used to load templates
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'The Daily Telegram'
    return render_template('index.html', title = title)

