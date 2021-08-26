"""Pascal triangle of n rows"""

def pascal(n_rows):
    triangle = []
    if n_rows == 0:
        return triangle
    triangle.append([1])
    for i in range(1, n_rows):
        prev_row = triangle[i - 1]
        curr_row = []
        curr_row.append(1)
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        curr_row.append(1)
        triangle.append(curr_row)
    return triangle

if __name__ == "__main__":
    print(pascal(5))
