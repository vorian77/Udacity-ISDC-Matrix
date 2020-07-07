import math
from math import sqrt
import numbers


def zeroes(height, width):
    """
    Creates a matrix of zeroes.
    """
    g = [[0.0 for _ in range(width)] for __ in range(height)]
    return Matrix(g)


def identity(n):
    """
    Creates a n x n identity matrix.
    """
    I = zeroes(n, n)
    for i in range(n):
        I.g[i][i] = 1.0
    return I


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise (NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here

        # process 1x1 matrix
        if self.h == 1:
            det = self.g[0][0]
            # check determinant is valid
            if det == 0:
                raise ValueError('The matrix is not invertable.')

            return det

        # process 2x2 matrix
        else:
            # process 2 x 2 matrix

            # set the 4 values of the matrix
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            # check - detriment is 0
            det = a * d - b * c
            if det == 0:
                raise ValueError('The matrix is not invertable.')

            return det


    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise (ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here

        # traverse through all values
        # sum values where the row = column
        total = 0
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                if i == j:
                    total += self.g[i][j]
        return total


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here

        if self.h == 1:
            # process 1 x 1 matrix
            value = self.g[0][0]

            # check for divide by 0
            if value == 0:
                raise ValueError('The matrix is not invertable.')

            # create new matrix
            new_matrix = zeroes(1, 1)

            # set the inverted value
            new_matrix[0][0] = 1 / value

            return new_matrix

        elif self.h == 2:
            # process 2 x 2 matrix

            # set the 4 values of the matrix
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]

            # check for determinant = 0
            determinant = a * d - b * c
            if determinant == 0:
                raise ValueError('The matrix is not invertable.')

            # create new matrix and set inverted values
            new_matrix = zeroes(2, 2)
            factor = 1 / determinant

            new_matrix[0][0] = d * factor
            new_matrix[0][1] = -b * factor
            new_matrix[1][0] = -c * factor
            new_matrix[1][1] = a * factor

            return new_matrix


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here

        # initialize a new matrix
        new_matrix = zeroes(self.w, self.h)

        # set the rows in the new matrix
        # as the columns in the current matrix
        for i in range(len(self.g[0])):
            for j in range(len(self.g)):
                new_matrix[i][j] = self.g[j][i]
        return new_matrix


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise (ValueError, "Matrices can only be added if the dimensions are the same")

        # TODO - your code here
        new_matrix = zeroes(self.h, self.h)
        for i in range(len(self.g)):
            for j in range(len(self.g)):
                new_matrix[i][j] = self.g[i][j] + other.g[i][j]
        return new_matrix


    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """

        # TODO - your code here
        new_matrix = zeroes(self.h, self.w)
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                new_matrix[i][j] = -self.g[i][j]
        return new_matrix


    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        # TODO - your code here


    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # TODO - your code here

        # return new matrix that is this matrix * other

        # init new matrix
        new_matrix = zeroes(self.h, other.w)

        # transpose other matrix to make calculations easier
        other_transposed = other.T()

        # calculate the dot product for each row, column
        # in the new matrix
        for i in range(len(new_matrix.g)):
            for j in range(len(new_matrix.g[i])):
                dot_product = 0
                for v1, v2 in zip(self.g[i], other_transposed[j]):
                    dot_product += v1 * v2
                    new_matrix[i][j] = dot_product
        return new_matrix



    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            # TODO - your code here

            # init new matrix
            new_matrix = zeroes(self.h, self.w)

            # set each value in the new matrix
            # as the corrosponding value in this matrix
            # times other
            for i in range(len(new_matrix.g)):
                for j in range(len(new_matrix.g[i])):
                    new_matrix[i][j] = other * self.g[i][j]
            return new_matrix
