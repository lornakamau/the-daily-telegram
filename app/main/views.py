from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_top_articles,get_keyword, get_breaking_news

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Getting sources
    sources = get_sources()
    breaking_news = get_breaking_news()
    title = 'The Daily Telegram'
    get_keyword = request.args.get('keyword_query')

    if get_keyword:
        return redirect(url_for('main.keyword', keyword_name=get_keyword))
    else:
        return render_template('index.html', title = title, sources=sources, breaking_news=breaking_news)

@main.route('/source/<sourcesId>')
def articles(sourcesId):
    '''
    View function that displays top stories from a particular source
    '''
    articles= get_top_articles(sourcesId)
    title = f"{sourcesId}"
    header = sourcesId.upper()
    get_keyword = request.args.get('keyword_query')

    if get_keyword:
        return redirect(url_for('main.keyword', keyword_name=get_keyword))
    else:
        return render_template('articles.html', title=title, header=header, article=articles)

@main.route('/search/<keyword_name>')
def keyword(keyword_name):
    '''
    View function to display the search results
    '''
    keyword_name_list = keyword_name.split(" ")
    keyword_name_format = "+".join(keyword_name_list)
    searched_keyword = get_keyword(keyword_name_format)
    title = f'{keyword_name.title()}'
    display_keyword = keyword_name.upper()

    return render_template('search.html', keyword = searched_keyword, title = title, display_keyword=display_keyword )
