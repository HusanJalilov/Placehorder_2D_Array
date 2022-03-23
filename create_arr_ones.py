def create_arr_ones(n,m):
    """
    Create 2D array NxM of ones
    Args:
        int: n
        int: m
    Returns:
        list: 2D list
    """
    a=0
    Matrix = [[1 for x in range(m)] for y in range(n)] 
    return Matrix
print(create_arr_ones(4,3))