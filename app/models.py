class News_source:
    """
    News_source class to define news_source objects
    """

    def __init__(self,id,name,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class Articles:
    """
    Articles class to define articles objects
    """

    def __init__(self,id,name,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        