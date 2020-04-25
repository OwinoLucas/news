from app import app
import urllib.request,json
from .models import news_source

News_source = news_source.News_source

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news_source(source):
    """
    Function that gets the json response to our url request
    """
    get_news_source_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['sources']:
            news_source_list = get_news_source_response['sources']
            news_source_results = process_results(news_source_list)

    return news_source_results

def process_results(news_source_list):
    """
    Function that processes the news_source result and transforms it to a list of objests
    
     Args:
        news_source_list: A list of dictionaries that contain news details

    Returns :
        news_source_results: A list of news objects
    """(
    news_source_results = []
    for news_source_item in news_source_list:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        category = news_source_item.get('category')
        country = news_source_item.get('country')

        if category:
            news_source_object = News_source(id,name,description,url,category,country)
            news_source_results.append(news_source_object)

    return news_source_results

