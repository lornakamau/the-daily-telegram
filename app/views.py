from flask import render_template #used to load templates
from app import app
from .request import get_sources, get_top_articles,search_keyword

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
    articles_with_images = get_top_articles(sourcesId)
    title = f"{sourcesId} articles"
    header = sourcesId.upper()
    
    return render_template('articles.html', title=title, header=header, articles=articles_with_images)

@app.route('/<keyword_name>')
def keyword(keyword_name):
    '''
    View function to display the search results
    '''
    keyword_name_list = keyword_name.split(" ")
    keyword_name_format = "+".join(keyword_name_list)
    searched_keyword = search_keyword(keyword_name_format)
    title = f'{keyword_name}'
    return render_template('search.html', keyword = searched_keyword, title = title)