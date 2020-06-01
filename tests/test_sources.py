import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources(1234, 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.', 'https://abcnews.go.com', 'general', 'en')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_initialization(self):
        '''
        Test initialization test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_source.name, 'ABC News' )
        self.assertEqual(self.new_source.language, 'en' )

if __name__ == '__main__':
    unittest.main()
