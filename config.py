import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'http://newsapi.org/v2/sources?&apiKey={}'
    NEWS_API_TOP_ARTICLES_BASE_URL = 'http://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_SEARCH_KEYWORD_BASE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy,publishedAt&pageSize=30&apiKey={}'
    NEWS_API_BREAKING_NEWS_BASE_URL = 'http://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY') 

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}