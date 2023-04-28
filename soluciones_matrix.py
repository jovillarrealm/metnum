from sympy import Matrix, shape, zeros


def takeDLU(A: Matrix):
    row, column = shape(A)
    D, L, U = zeros(row, column), zeros(row, column), zeros(row, column)

    for i in range(row):
        for j in range(column):
            if i == j:
                D[i, j] = A[i, j]
            elif i > j:
                L[i, j] = A[i, j]
            elif i < j:
                U[i, j] = A[i, j]
    L=-1*L
    U=-1*U
    return D, L, U




