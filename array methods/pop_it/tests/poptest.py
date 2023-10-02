import unittest
from pop import canyoupopit

class TestCanYouPopItMethod(unittest.TestCase):
    def setUp(self):
        self.list = [1, 2, 3, 4, 5]

    def test_pop_last_element(self):
        popped_element = can_you_pop_it(self.list)
        self.assertEqual(popped_element, 5, "The popped element should be the last one.")
        self.assertEqual(self.list, [1, 2, 3, 4], "The list should not contain the popped element.")

    def test_pop_specific_index(self):
        popped_element = can_you_pop_it(self.list, 2)
        self.assertEqual(popped_element, 3, "The popped element should be the one at the specified index.")
        self.assertEqual(self.list, [1, 2, 4, 5], "The list should not contain the popped element.")

    def test_pop_empty_list(self):
        empty_list = []
        with self.assertRaises(IndexError, msg="Popping from an empty list should raise an IndexError."):
            can_you_pop_it(empty_list)

if __name__ == '__main__':
    unittest.main()
