def create_arr_full_row_num(n,m):
    """
    Create 2D array NxM of ones
    Args:
        int: n
        int: m
    Returns:
        list: 2D list

Input: n=4, m = 3
Output:
    [[0, 0, 0], 
     [1, 1, 1], 
     [2, 2, 2], 
     [3, 3, 3]]

    """
    a=0
    Matrix = [[1 for x in range(m)] for y in range(n)] 
    return Matrix
print(create_arr_full_row_num(4,3))

