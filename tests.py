import unittest
import urlShortener
from unittest.mock import patch

class MyTestCase(unittest.TestCase):
    def test_shorten(self):
        with patch('random.random.choices') as mock_random:
            mock_random.return_value = 'test'
            print(urlShortener.shortenUrl('TEST'))

if __name__ == '__main__':
    unittest.main()
