from app import app
import urllib.request,json
from .models import news_source
from .models import articles

News_source = news_source.News_source

# Getting api key
apiKey = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
base_urll = app.config["NEWS_API_BASE_URLL"]

def get_news_source(sources):
    """
    Function that gets the json response to our url request
    """
    get_news_source_url = base_url.format(sources,apiKey)

    with urllib.request.urlopen(get_news_source_url) as url:
        get_news_source_data = url.read()
        get_news_source_response = json.loads(get_news_source_data)

        news_source_results = None

        if get_news_source_response['articles']:
            news_source_list = get_news_source_response['articles']
            news_source_results = process_results(news_source_list)

    return news_source_results

def process_results(news_source_list):
    """
    Function that processes the news_source result and transforms it to a list of objests
    
     Args:
        news_source_list: A list of dictionaries that contain news details

    Returns :
        news_source_results: A list of news objects
    """
    news_source_results = []

    for news_source_item in news_source_list:
        id = news_source_item.get('id')
        name = news_source_item.get('name')
        title = news_source_item.get('title')
        description = news_source_item.get('description')
        url = news_source_item.get('url')
        publishedAt = news_source_item.get('publishedAt')
        content = news_source_item.get('content')

        if content:
            news_source_object = News_source(id,name,title,description,url,publishedAt,content)
            news_source_results.append(news_source_object)

    return news_source_results

def get_articles(category):
    """
    Fuction to get article json from request
    """
    get_articles_url = base_urll.format(category,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        article_response = json.loads(articles_data)

        articles_object = None
        if article_response:
            id = article_response.get('id')
            name = article_response.get('name')
            description = article_response.get('description')
            url = article_response.get('url')
            category = article_response.get('category')
            language = article_response.get('language')

            if language =='en':
                articles_object = Articles(id,name,description,url,category,language)


    return articles_object


    



