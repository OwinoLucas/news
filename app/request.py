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

