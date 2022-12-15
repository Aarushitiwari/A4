import unittest
from unittest.mock import MagicMock

import sys
sys.path.append('./service')
import book_pb2 as pb2
from inventory_client import InventoryClient
from get_book_titles import get_book_titles

# Create a mock of the InventoryClient class
mock_client = MagicMock(spec=InventoryClient)

# Set up the mock to return a specific response when the GetBook method is called
mock_client.get_books.return_value = pb2.Book(title="Book 1")


class TestGetBookTitles(unittest.TestCase):
    def test_get_book_titles_with_mock(self):
        # Call the get_book_titles function with the mock client
        titles = get_book_titles(mock_client, ['12345', '23456'])

        self.assertEqual(titles, ["Book 1", "Book 1"])

    def test_get_book_titles_with_server(self):
        # Create an instance of the InventoryClient class
        client = InventoryClient()

        # Call the get_book_titles function with the client
        titles = get_book_titles(client, ['12345', '23456'])

        self.assertEqual(titles, ["Book 1", "Book 2"])


if __name__ == '__main__':
    unittest.main()

