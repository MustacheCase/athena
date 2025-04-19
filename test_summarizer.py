import unittest
from unittest.mock import patch, Mock
from summarizer import summarize_article

class TestSummarizer(unittest.TestCase):

    @patch('summarizer.model.generate_content')
    def test_summarize_article(self, mock_generate_content):
        # Mock the response from the Generative AI model
        mock_response = Mock()
        mock_response.text = "This is a professional summary."
        mock_generate_content.return_value = mock_response

        # Call the function
        title = "Sample Article"
        content = "This is the content of the sample article."
        summary = summarize_article(title, content)

        # Assertions
        self.assertEqual(summary, "This is a professional summary.")
        mock_generate_content.assert_called_once_with(
            "TL;DR Professional summary of 'Sample Article':\n\nThis is the content of the sample article."
        )

if __name__ == '__main__':
    unittest.main()