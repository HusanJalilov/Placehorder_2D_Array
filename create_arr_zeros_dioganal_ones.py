from numpy import matrix


def create_arr_zeros_dioganal_ones(n):
    """
    Create 2D array NxN of ones. Array border is zeros.
    Args:
        int: n
    Returns:
        list: 2D list
    """
    
    z = [[0 for x in range(n)] for y in range(n)]    
    for i in range(n):
        z[i][i]=1
    return z
print(create_arr_zeros_dioganal_ones(7))