from sympy import Matrix

A = Matrix([
    [4, 3, -2, -7],
    [3, 12, 8, -3],
    [2, 3, -9, 3],
    [1, - 2, - 5, 6],]
)

# Returns (L, U, perm) where L is a lower triangular matrix with unit diagonal, U is an upper triangular matrix, and perm is a list of row swap index pairs. If A is the original matrix, then A = (L*U).permuteBkwd(perm), and the row permutation matrix P such that can be computed by P = eye(A.rows).permuteFwd(perm).
print(A.LUdecomposition())
print()

# Compute a fraction-free LU decomposition.
#Returns 4 matrices P, L, D, U such that PA = L D**-1 U. If the elements of the matrix belong to some integral domain I, then all elements of L, D and U are guaranteed to belong to I.
print(A.LUdecompositionFF())
print()

#Compute the PLU decomposition of the matrix. Returns one matrix.
print(A.LUdecomposition_Simple())
