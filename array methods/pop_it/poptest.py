import unittest
from pop import can_you_pop_it  # Change 'custom_pop' to 'pop'

class TestCanYouPopIt(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        with self.assertRaises(IndexError):
            can_you_pop_it(empty_list)

    def test_single_element_list(self):
        single_element_list = [42]
        popped_item = can_you_pop_it(single_element_list)
        self.assertEqual(popped_item, 42)
        self.assertEqual(single_element_list, [])

    def test_multiple_elements_list(self):
        my_list = [1, 2, 3, 4, 5]
        popped_item = can_you_pop_it(my_list)
        self.assertEqual(popped_item, 5)
        self.assertEqual(my_list, [1, 2, 3, 4])

    @unittest.expectedFailure
    def test_prevent_builtin_pop(self):
        empty_list = []
        with self.assertRaises(IndexError):
            empty_list.pop()

if __name__ == '__main__':
    unittest.main()
