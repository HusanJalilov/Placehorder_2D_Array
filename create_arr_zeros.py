def create_arr_zeros(n,m):
    """
    Create 2D array NxM of zeros
    Args:
      	int: n
      	int: m
    Returns:
      	list: 2D list
    """
    a=0
    Matrix = [[0 for x in range(m)] for y in range(n)] 
    return Matrix