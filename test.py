import time
import unittest
from ddt import file_data, ddt
from web_keys.keys import Key


@ddt
class Case(unittest.TestCase):
    @file_data("test_data/web.yaml")
    def test_search(self, common, text):
        key = Key(common["browser_type"])
        key.open(common["url"])
        key.input(**common["input"], text=text)
        key.click(**common["click"])
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()