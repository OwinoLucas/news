from flask import render_template
from app import app
from .request import get_news_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting news_source category
    source_news = get_news_source('cnn')
    print(source_news)
    title = 'Home - Welcome to The best News Website Online'
    return render_template('index.html', title = title, cnn = source_news)

@app.route('/news_source/<news_source_id>')
def news_source(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news_source.html',id = news_source_id)