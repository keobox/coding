"""Check if a matrix is a submatrix"""

def check_assumptions(matrix, submatrix):
    """ Checks assumption about matrices."""
    less_rows = len(matrix) > len(submatrix)
    mc = len(matrix[0])
    # all matrix columns have the same size
    assert all(len(m) == mc for m in matrix) is True
    # all submatrix columns have the same size
    sc = len(submatrix[0])
    assert all(len(s) == sc for s in submatrix) is True
    less_cols = mc > sc
    assert less_rows or less_cols is True

def check_submatrix(matrix, submatrix):
    """ Checks a submatrix of matrix"""
    check_assumptions(matrix, submatrix)
    res = []
    for col_submatrix in submatrix:
        for col_matrix in matrix:
            n = len(col_submatrix)
            m = len(col_matrix)
            for i in range(n):
                slice_list = col_matrix[i:n + i]
                if slice_list == col_submatrix:
                    res.append(True)
    return len(res) == len(submatrix) and all(res)
    
A = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
B = [[4, 5], [7, 8]]
assert check_submatrix(A, B) is True

A = [[0, 1, 2], [3, 9, 9], [6, 7, 8]]
assert check_submatrix(A, B) is False

print("Tests passed")
