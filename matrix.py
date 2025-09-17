def get_matrix(name):
    rows = int(input(f"Enter number of rows in {name}: "))
    cols = int(input(f"Enter number of columns in {name}: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError("Number of elements in row doesn't match column count.")
        matrix.append(row)
    return matrix, rows, cols

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(val)
        result.append(row)
    return result

def transpose_matrix(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def scalar_multiply_matrix(A, scalar):
    return [[scalar * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def matrix_equal(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != B[i][j]:
                return False
    return True

def determinant(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        submatrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * determinant(submatrix)
    return det

def print_matrix(matrix, name="Result"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    while True:
        print("\nMatrix Calculator Menu:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Scalar Multiplication")
        print("6. Determinant")
        print("7. Check Equality")
        print("8. Exit")
        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '7']:
            A, r1, c1 = get_matrix("Matrix A")
            B, r2, c2 = get_matrix("Matrix B")

        if choice == '1':
            if r1 == r2 and c1 == c2:
                result = add_matrices(A, B)
                print_matrix(result, "Addition Result")
            else:
                print("Error: Matrices must be of same dimensions for addition.")
        elif choice == '2':
            if r1 == r2 and c1 == c2:
                result = subtract_matrices(A, B)
                print_matrix(result, "Subtraction Result")
            else:
                print("Error: Matrices must be of same dimensions for subtraction.")
        elif choice == '3':
            if c1 == r2:
                result = multiply_matrices(A, B)
                print_matrix(result, "Multiplication Result")
            else:
                print("Error: Number of columns of A must equal number of rows of B for multiplication.")
        elif choice == '4':
            A, r1, c1 = get_matrix("Matrix")
            result = transpose_matrix(A)
            print_matrix(result, "Transpose Result")
        elif choice == '5':
            A, r1, c1 = get_matrix("Matrix")
            scalar = float(input("Enter scalar value: "))
            result = scalar_multiply_matrix(A, scalar)
            print_matrix(result, "Scalar Multiplication Result")
        elif choice == '6':
            A, r1, c1 = get_matrix("Matrix")
            if r1 != c1:
                print("Error: Determinant can only be calculated for square matrices.")
            else:
                det = determinant(A)
                print(f"Determinant: {det}")
        elif choice == '7':
            if r1 == r2 and c1 == c2:
                equal = matrix_equal(A, B)
                print(f"Matrices are {'equal' if equal else 'not equal'}.")
            else:
                print("Error: Matrices must be of same dimensions to check equality.")
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
