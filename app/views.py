from flask import render_template,request,redirect,url_for
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
    search_keyword = request.args.get('keyword_query')

    if search_keyword:
        return redirect(url_for('keyword', keyword_name=search_keyword))
    else:
        return render_template('index.html', title = title, sources=sources)

@app.route('/<sourcesId>')
def articles(sourcesId):
    '''
    View function that displays top stories from a particular source
    '''
    articles= get_top_articles(sourcesId)
    title = f"{sourcesId}"
    header = sourcesId.upper()
    search_keyword = request.args.get('keyword_query')

    if search_keyword:
        return redirect(url_for('keyword', keyword_name=search_keyword))
    else:
        return render_template('articles.html', title=title, header=header, articles=articles)

@app.route('/search/<keyword_name>')
def keyword(keyword_name):
    '''
    View function to display the search results
    '''
    keyword_name_list = keyword_name.split(" ")
    keyword_name_format = "+".join(keyword_name_list)
    searched_keyword = search_keyword(keyword_name_format)
    title = f'{keyword_name}'
    return render_template('search.html', keyword = searched_keyword, title = title)