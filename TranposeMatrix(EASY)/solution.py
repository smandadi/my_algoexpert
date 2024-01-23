#!/usr/bin/env python3

# You're given a 2D array of integers matrix. Write a function that returns the transpose of the matrix.
# The transpose of a matrix is a flipped version of the original matrix across its main diagonal (which runs from top-left to bottom-right);
# it switches the row and column indices of the original matrix.
# You can assume the input matrix always has at least 1 value; however its width and height are not necessarily the same.

# space: O(c*r) and time: O(c*r)
def transposeMatrix(matrix):

    col = len(matrix[0])
    rows = len(matrix)

    output = [[0] * rows for i in range(col)]  # space: O(c * r) and time O(c * r)

    for i in range(rows):
        for j in range(col):
            output[j][i] = matrix[i][j]         
    
    return output


if __name__ == "__main__":
    x = transposeMatrix([[1, 2, 3]])
    assert x == [[1],[2],[3]]