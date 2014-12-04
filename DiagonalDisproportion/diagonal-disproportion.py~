'''
 You are to calculate the diagonal disproportion of a square
 matrix. The diagonal disproportion of a square matrix is the sum of
 the elements of its main diagonal minus the sum of the elements of
 its collateral diagonal. The main and collateral diagonals of a
 square matrix are shown in figures 1 and 2 respectively.

 The elements of the main diagonal are shown in green in figure 1, and
 the elements of the collateral diagonal are shown in cyan in figure
 2.

Given a String[] matrix, return its diagonal disproportion. The j'th
character of the i'th element of matrix should be treated as the
element in the i'th row and j'th column of the matrix.
'''

class DiagonalProportion:
    def getDisproportion(self, matrix):
        def trace(matrix):
            return sum([row[i] for i, row in enumerate(matrix)])

        return trace(matrix) - trace([x[::-1] for x in matrix])

    
