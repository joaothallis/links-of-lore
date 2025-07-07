import unittest
from unittest.mock import patch
import sys
import os
import requests

# Add the parent directory to the sys.path to allow importing fetch_title
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fetch_title import fetch_title

class TestFetchTitle(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_title_success(self, mock_get):
        # Mock a successful response
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.text = "<html><head><title>Test Title</title></head><body></body></html>"
        mock_get.return_value = mock_response

        url = "http://example.com"
        title = fetch_title(url)
        self.assertEqual(title, "Test Title")
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_fetch_title_no_title(self, mock_get):
        # Mock a response with no title tag
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.text = "<html><head></head><body></body></html>"
        mock_get.return_value = mock_response

        url = "http://example.com"
        title = fetch_title(url)
        self.assertEqual(title, "") # BeautifulSoup returns empty string if no title
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_fetch_title_http_error(self, mock_get):
        # Mock an HTTP error response
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        url = "http://example.com/nonexistent"
        title = fetch_title(url)
        self.assertIn("Error fetching title", title)
        self.assertIn("404 Not Found", title)
        mock_get.assert_called_once_with(url)

    @patch('requests.get')
    def test_fetch_title_connection_error(self, mock_get):
        # Mock a connection error
        mock_get.side_effect = requests.exceptions.ConnectionError("DNS lookup failed")

        url = "http://nonexistent-domain.com"
        title = fetch_title(url)
        self.assertIn("Error fetching title", title)
        self.assertIn("DNS lookup failed", title)
        mock_get.assert_called_once_with(url)

if __name__ == '__main__':
    unittest.main()
