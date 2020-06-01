import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Stan Schroeder', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'https://abcnews.go.com', '2020-05-16T00:34:00Z', 'https://mashable.com/article/bitcoin-halving-2020/')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_article, Articles))

    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_article.author, 'Stan Schroeder' )
        self.assertEqual(self.new_article.imageurl, 'https://abcnews.go.com' )

if __name__ == '__main__':
    unittest.main()