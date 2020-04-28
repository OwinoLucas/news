#from app import create_app
import urllib.request,json
from .models import News_source
from .models import Articles

#News_source = news_source.News_source
#Articles = articles.Articles

# Getting api key
apiKey = None

# Getting the news base url
base_url = None
base_urll = None

def configure_request(app):
    global apiKey,base_url,base_urll
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_urll = app.config['NEWS_API_BASE_URLL']



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
        urlToImage = news_source_item.get('urlToImage')
        publishedAt = news_source_item.get('publishedAt')
        content = news_source_item.get('content')

        if urlToImage:
            news_source_object = News_source(id,name,title,description,url,urlToImage,publishedAt,content)
            news_source_results.append(news_source_object)

    return news_source_results


def get_articles(country):
    """
    Fuction to get article json from request
    """
    get_articles_url = base_urll.format(country,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        
        articles_results = None
        if articles_response['articles']:
            articles_list = articles_response['articles']
            articles_results = process_result(articles_list)

    return articles_results


def process_result(articles_list):
    """
    Function that processes the articles result and transforms it to a list of objests
    
     Args:
        articles_list: A list of dictionaries that contain articles details

    Returns :
        articles_results: A list of articles objects
    """
    articles_results = []
    
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')
        if urlToImage:
            articles_object = Articles(id,name,title,description,url,urlToImage,publishedAt,content)
            articles_results.append(articles_object)

    return articles_results

#def search_news_source(source_name):
   # search_news_source_url = 'http://newsapi.org/v2/search?apiKey={}&query={}'.format(apiKey,source_name)
   # with urllib.request.urlopen(search_news_source_url) as url:
    #    search_news_source_data = url.read()
    #    search_news_source_response = json.loads(search_news_source_data)

     #   search_news_source_results = None

     #   if search_news_source_response['articles']:
      #      search_news_source_list = search_news_source_response['articles']
      #      search_news_source_results = process_resultss(search_news_source_list)

    #return search_news_source_results

#def process_resultss(search_news_source_list):
 #   """
 #   Function that processes the search_news_source result and transforms it to a list of objests
    
 #    Args:
 #       search_news_source_list: A list of dictionaries that contain news details

  #  Returns :
  #      search_news_source_results: A list of news objects
 #   """
 #   search_news_source_results = []

  #  for search_news_source_item in search_news_source_list:
 #       id = search_news_source_item.get('id')
 #       name = search_news_source_item.get('name')
  #      title = search_news_source_item.get('title')
 #       description = search_news_source_item.get('description')
 #       url = search_news_source_item.get('url')
 #       urlToImage = search_news_source_item.get('urlToImage')
 #       publishedAt = search_news_source_item.get('publishedAt')
 #       content = search_news_source_item.get('content')

 #       if urlToImage:
#            search_news_source_object = News_source(id,name,title,description,url,urlToImage,publishedAt,content)
 #           search_news_source_results.append(search_news_source_object)

 #   return search_news_source_results




    



