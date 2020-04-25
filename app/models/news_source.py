class News_source:
    """
    News_source class to define news_source objects
    """

    def __init__(self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country