import unittest
from models import news_source
News_source = news_source.News_source

class News_sourceTest(unittest.TestCase):
    """
    Test Class to test behaviour of the news class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_news_source = News_source('id','ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com', 'general', 'us')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source, News_source))


if __name__ == '__main__':
    unittest.main()