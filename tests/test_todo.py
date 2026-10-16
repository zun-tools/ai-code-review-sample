import unittest

from todo import list_items


class TestListItems(unittest.TestCase):
    def test_keeps_order(self):
        self.assertEqual(list_items(["b", "a"]), ["b", "a"])

    def test_sort(self):
        self.assertEqual(list_items(["b", "a"], sort=True), ["a", "b"])

    def test_filter(self):
        self.assertEqual(list_items(["bug", "idea"], keyword="bu"), ["bug"])


if __name__ == "__main__":
    unittest.main()
