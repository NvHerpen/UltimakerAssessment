import unittest
from urlShortener import shortenUrl
from unittest import mock

class MyTestCase(unittest.TestCase):
    @mock.patch('urlShortener.random')
    def test_shorten(self, mocked_random):
        shortenUrl("abc")
        mocked_random.choices.assert_called_once()

if __name__ == '__main__':
    unittest.main()
