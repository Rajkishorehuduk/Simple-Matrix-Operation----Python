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

def print_matrix(matrix, name="Result"):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    A, r1, c1 = get_matrix("Matrix A")
    B, r2, c2 = get_matrix("Matrix B")

    print("\nChoose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter choice (1/2/3): ")

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
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()

