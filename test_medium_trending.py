import unittest
from unittest.mock import patch, Mock
from medium_trending import get_top_tech_articles

class TestMediumTrending(unittest.TestCase):

    @patch('medium_trending.requests.get')
    @patch('medium_trending.feedparser.parse')
    def test_get_top_tech_articles(self, mock_parse, mock_get):
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.content = b''
        mock_get.return_value = mock_response

        # Mock the parsed feed
        class MockEntry:
            def __init__(self, title, link, summary):
                self.title = title
                self.link = link
                self.summary = summary

        # Create mock entries
        mock_entries = [
            MockEntry('Article 1', 'http://example.com/article1', 'Summary of article 1'),
            MockEntry('Article 2', 'http://example.com/article2', 'Summary of article 2')
        ]

        # Create a mock feed object with the entries
        mock_feed = Mock()
        mock_feed.entries = mock_entries
        mock_parse.return_value = mock_feed

        # Call the function
        articles = get_top_tech_articles()

        # Assertions
        self.assertEqual(len(articles), 2)
        self.assertEqual(articles[0]['title'], 'Article 1')
        self.assertEqual(articles[0]['link'], 'http://example.com/article1')
        self.assertEqual(articles[0]['content'], 'Summary of article 1')
        self.assertEqual(articles[1]['title'], 'Article 2')
        self.assertEqual(articles[1]['link'], 'http://example.com/article2')
        self.assertEqual(articles[1]['content'], 'Summary of article 2')

if __name__ == '__main__':
    unittest.main()