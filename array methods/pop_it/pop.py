def can_you_pop_it(input_list):
    """
    Simulates the behavior of the pop method for lists by removing and returning the last item in the list.

    Args:
        input_list (list): The list from which to pop an item.

    Returns:
        any: The popped item.

    Raises:
        IndexError: If the list is empty.

    Example:
        >>> my_list = [1, 2, 3, 4, 5]
        >>> popped_item = can_you_pop_it(my_list)
        >>> print("Popped item:", popped_item)
        >>> print("Updated list:", my_list)
        Popped item: 5
        Updated list: [1, 2, 3, 4]

    Your code to use the can_you_pop_it function should go below this comment.
    """
    
    
    arr_size = len(input_list)
    

    if arr_size == 0:
        """
            raise an idex error if the array is empty
        """
        raise IndexError
        
    elif arr_size == 1:
        """
            if array has one value, remove the one value and return the removed value while modifying the array
        """
        last = input_list[-1]
        input_list.remove(last)
        return last

        

    elif arr_size > 1:

        """
            if array has more than one value, remove the one value and return the removed value while modifying the array
        """

        """
            revise this to account for when there are 2 of the same elements last element in the list.
        """
        
        last = input_list[-1]
        input_list.remove(last)
        return last
    
    

    


   
        
    


    
