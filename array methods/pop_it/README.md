# `can_you_pop_it` Function

The `can_you_pop_it` function is a custom Python method that simulates the behavior of the `pop` method for lists. It allows you to remove and return the last item from a list. This README provides instructions on how to use this function and run the included test.


Here's an example of how to use the `can_you_pop_it` function:

```python
from custom_pop import can_you_pop_it

my_list = [1, 2, 3, 4, 5]
popped_item = can_you_pop_it(my_list)

print("Popped item:", popped_item)
print("Updated list:", my_list)
```
### Test Cases

The included test script (`poptest.py`) performs the following test cases:

1. **Empty List Test**: Checks the behavior of the `can_you_pop_it` function when an empty list is provided as input. It verifies that the function correctly raises an `IndexError` because you cannot pop an item from an empty list.

2. **Single Element List Test**: Checks the behavior of the `can_you_pop_it` function when a list with a single element is provided as input. It verifies that the function correctly pops the last item from the list and that the list becomes empty afterward.

3. **Multiple Elements List Test**: Checks the behavior of the `can_you_pop_it` function when a list with multiple elements is provided as input. It verifies that the function correctly pops the last item from the list and that the list is updated to remove the popped item.

## Test

Included in this repository is a test script that verifies the functionality of the `can_you_pop_it` function. To run the test, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where this repository is located.

3. Run the test script using the following command:

   ```bash
   python poptest.py

   or

   python3 poptest.py
   ```

   This command will execute the test and provide output indicating whether the `can_you_pop_it` function behaves as expected.

## Contributions

If you encounter any issues or want to contribute to the development of this function, please open an issue or create a pull request on the GitHub repository.
