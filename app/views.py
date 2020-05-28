from flask import render_template #used to load templates
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting sources
    sources = get_sources()
    title = 'The Daily Telegram'
    return render_template('index.html', title = title, sources = sources)
