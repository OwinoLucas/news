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
        self.new_news_source = News_source('id','ABC News','States partly reopen as US virus deaths top 50,000', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com', '2020-04-25T04:39:19Z', 'More than 20,000 people have now died with coronavirus in UK hospitals, the Department of Health has announced.\r\nThe latest figures showed a total of 20,319 deaths in the UK, up by 813 on the previous day.')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news_source, News_source))


if __name__ == '__main__':
    unittest.main()