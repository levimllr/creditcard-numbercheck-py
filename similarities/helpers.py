from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    # The purpose of this function is to calculate edit distance (or cost) from strings a to b.

    # Here we define a couple of variables that will save us a few keystrokes.
    alen = len(a) + 1
    blen = len(b) + 1

    # Here we generate a matrix (or 2D array) of null elements, based on the fact that matrix[0][0] = (0, None), as there is no editing cost in going from "" to "".
    matrix = [[(0, None)] * blen for i in range(alen)]

    # Now we add values for the base cases. matrix[1][1]
    # The first row, save for matrix[0][0] consists of incrementing insertions ("" to any string only requires insertions).
    # Similarly, the first column save matrix[0][0] consists of incrementing deletions (any string to "" only requires deletions).
    if not (a == "" or b == ""):
        if a[0] != b[0]:
            matrix[1][1] = (1, Operation.SUBSTITUTED)
    for j in range(1, alen):
        matrix[j][0] = (j, Operation.DELETED)
    for k in range(1, blen):
        matrix[0][k] = (k, Operation.INSERTED)

    # Now things get interesting. We are going to iterate over each cell in the matrix, going row by row and and column by column.
    for l in range(1, alen):

        for m in range(1, blen):

            # The following variables store the cost of each operation. The cost is simply the number of steps it takes to edit string a so that it matches string b.
            delcost = matrix[l - 1][m][0] + 1
            inscost = matrix[l][m - 1][0] + 1
            # The cost of substituting a character will be the same as the previous cell on the diagonal, unless the lth/mth character in question for strings a and b are not the same.
            subcost = matrix[l - 1][m - 1][0]
            if a[l - 1] != b[m - 1]:
                subcost += 1

            # The cost inputted into the tuple of the cell is the minimum cost across deletions, insertions, and substitutions.
            cost = min(delcost, inscost, subcost)
            # The operation inputted into the tuple of the cell is the one associate with the minimum cost.
            if cost == delcost:
                oper = Operation.DELETED
            elif cost == inscost:
                oper = Operation.INSERTED
            else:
                oper = Operation.SUBSTITUTED

            # Now we finally get to update value of the tuple in our matrix!
            matrix[l][m] = (cost, oper)

    # A few prints for debugging...
#    print(matrix)
#    print(matrix[3][1])
#    print(matrix[2][1])
#    print(matrix[4][3])

    return matrix

# Gotta run this dude!!
# distances("", "")