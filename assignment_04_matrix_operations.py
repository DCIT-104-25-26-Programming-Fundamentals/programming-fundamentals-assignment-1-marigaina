# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            sum_product = 0
            for k in range(cols_a):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_product)
        result.append(new_row)
    return result

#main program to demonstrate the matrix operations
print("Matrix Operations Program")
print("-------------------------")

# Part A: Transpose a Matrix
print("\nPart A: Transpose a Matrix")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

print("Original Matrix:")
for row in matrix:
    print(" ".join(map(str, row)))

transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(" ".join(map(str, row)))

#part B: Add Two Matrices
print("\nPart B: Add Two Matrices")
rows = int(input("Enter number of rows for both matrices: "))
cols = int(input("Enter number of columns for both matrices: "))
matrix_a = []
matrix_b = []

print("Enter elements for Matrix A:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix_a.append(row)

print("Enter elements for Matrix B:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix_b.append(row)

result = add_matrices(matrix_a, matrix_b)
print("Result of Matrix Addition:")
for row in result:
    print(" ".join(map(str, row)))

#part C: Multiply Two Matrices
print("\nPart C: Multiply Two Matrices")
rows_a = int(input("Enter number of rows for Matrix A: "))
cols_a = int(input("Enter number of columns for Matrix A: "))
rows_b = int(input("Enter number of rows for Matrix B: "))
cols_b = int(input("Enter number of columns for Matrix B: "))

if cols_a != rows_b:
    print("Error: Incompatible matrix dimensions")
else:
    matrix_a = []
    matrix_b = []

    print("Enter elements for Matrix A:")
    for i in range(rows_a):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix_a.append(row)

    print("Enter elements for Matrix B:")
    for i in range(rows_b):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix_b.append(row)

    result = multiply_matrices(matrix_a, matrix_b)
    print("Result of Matrix Multiplication:")
    for row in result:
        print(" ".join(map(str, row)))