from flask import render_template
from app import app
from .request import get_news_source, get_articles

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting news_source category
    abc_news = get_news_source('abc-news')
    cnn_news = get_news_source('cnn')
    time_news = get_news_source('time')
    nbc_news = get_news_source('nbc-news')
    fox_news = get_news_source('fox-news')
    espn_news = get_news_source('espn')
    the_wall_street_journal = get_news_source('the-wall-street-journal')
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title, abc = abc_news, cnn = cnn_news, time = time_news , nbc = nbc_news, fox = fox_news, wallstreet = the_wall_street_journal, espn = espn_news)

@app.route('/articles')
def articles():

    '''
    View articles page function that returns the articles details page and its data
    '''
    category_articles = get_articles('business')
    title = 'Here are articles from various fields'
    return render_template('articles.html',title = title, business = category_articles )


    #business_articles = get_articles('business')
    #entertainment_articles = get_articles('entertainment')
    #general_articles = get_articles('general')
    #health_articles = get_articles('health')
    #science_articles = get_articles('science')
    #sports_articles = get_articles('sports')
    #technology_articles = get_articles('technology')