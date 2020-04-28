from flask import render_template
from . import main
from ..request import get_news_source, get_articles

# Views
@main.route('/')
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
    title = 'Home - Welcome to The best News source Website Online'

    #search_news_source = request.args.get('source_query')

    #if search_news_source:
    #    return redirect(url_for('search',source_name = search_news_source))
    #else:
    return render_template('index.html', title = title, abc = abc_news, cnn = cnn_news, time = time_news , nbc = nbc_news, fox = fox_news, wallstreet = the_wall_street_journal, espn = espn_news)

@main.route('/articles')
def articles():

    '''
    View articles page function that returns the articles details page and its data
    '''
    us_articles = get_articles('us')
    uk_articles = get_articles('gb')
    
    title = 'Here are articles from various fields'
    return render_template('articles.html',title = title, us = us_articles,gb = uk_articles)

#@app.route('/search/<source_name>')
#def search(source_name):
   # """
    #FUction to display search results
   # """
   # source_name_list = source_name.split(" ")
   # source_name_format = "+".join(source_name_list)
   # searched_source = search_news_source(source_name_format)
  #  title = f'search results for {source_name}'
  #  return render_template('search.html', sources = searched_source)

    