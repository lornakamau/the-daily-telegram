from flask import render_template #used to load templates
from app import app
from .request import get_sources, get_top_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting sources
    sources = get_sources()
    title = 'The Daily Telegram'
    return render_template('index.html', title = title, sources=sources)

@app.route('/<sourcesId>')
def articles(sourcesId):
    '''
    View function that displays top stories from a particular source
    '''
    articles = get_top_articles(sourcesId)
    title = f"{sourcesId} articles"
    header = sourcesId.upper()
    
    return render_template('articles.html', title=title, header=header, articles=articles)