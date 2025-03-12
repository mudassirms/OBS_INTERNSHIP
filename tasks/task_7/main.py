import numpy as np

def input_matrix(rows, cols, name):
    print(f"Enter the elements of matrix {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} values.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return np.array(matrix)

def matrix_multiplication(A, B):
    try:
        result = np.dot(A, B)
        return result
    except ValueError:
        return "Matrix multiplication not possible. Check dimensions."

# Take matrix dimensions as input
rows_A = int(input("Enter the number of rows for Matrix A: "))
cols_A = int(input("Enter the number of columns for Matrix A: "))

rows_B = int(input("Enter the number of rows for Matrix B: "))
cols_B = int(input("Enter the number of columns for Matrix B: "))

# Ensure matrices are compatible for multiplication
if cols_A != rows_B:
    print("Matrix multiplication not possible. The number of columns in A must match the number of rows in B.")
else:
    # Input matrices from the user
    A = input_matrix(rows_A, cols_A, "A")
    B = input_matrix(rows_B, cols_B, "B")

    # Perform multiplication
    result = matrix_multiplication(A, B)

    # Display result
    print("\nMatrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    print("\nResultant Matrix:")
    print(result)
