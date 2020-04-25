class News_source:
    """
    News_source class to define news_source objects
    """

    def __init__(self,id,name,title,description,url,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.publishedAt = publishedAt
        self.content = content