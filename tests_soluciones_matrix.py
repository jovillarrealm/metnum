
from sympy import Matrix, init_printing
from soluciones_matrix import *

init_printing(use_unicode=True)


A = Matrix([
    [9, 6, -3],
    [3, 18, 7],
    [-6, 8, 12],])


A = Matrix([
    [4, 3, -2, -7],
    [3, 12, 8, -3],
    [2, 3, -9, 3],
    [1, - 2, - 5, 6],]
)


# Returns (L, U, perm) where L is a lower triangular matrix with unit diagonal, U is an upper triangular matrix, and perm is a list of row swap index pairs. If A is the original matrix, then A = (L*U).permuteBkwd(perm), and the row permutation matrix P such that can be computed by P = eye(A.rows).permuteFwd(perm).
L, U, perm = A.LUdecomposition()
print(L, U, perm)
print()

# Internamente usa LU para LUx = b -> A.LUsolve(b)
print(A.LUsolve(Matrix([20, 18, 31, 12])))
print()

# A-> D-L-U
print(takeDLU(A))
print()



