This is a Python program that implements a Matrix Calculator via a command-line interface. 🔢 It allows users to input matrices and perform various linear algebra operations on them based on their menu selection.

Matrix Calculator Description
The program is structured with several functions, each handling a specific matrix operation or utility:

Input and Output:

get_matrix(name): Prompts the user for the number of rows and columns, then takes row inputs (space-separated integers) to build a matrix. It includes a check to ensure the correct number of elements per row.

print_matrix(matrix, name): Formats and displays the resulting matrix to the user.

Operations:

add_matrices(A, B) and subtract_matrices(A, B): Perform element-wise addition and subtraction.

multiply_matrices(A, B): Performs matrix multiplication, using a list comprehension with a nested sum() to calculate the dot product for each cell.

transpose_matrix(A): Swaps rows and columns to find the transpose.

scalar_multiply_matrix(A, scalar): Multiplies every element in the matrix by a given scalar value.

Properties:

determinant(matrix): Calculates the determinant using a recursive cofactor expansion method. It includes a base case for 2×2 matrices.

matrix_equal(A, B): Checks if two matrices have the same dimensions and if all corresponding elements are identical.

Main Logic (main):

Presents an interactive menu (1-8) for selecting an operation.

Includes dimension checks for each operation (e.g., matrices must be the same size for addition, and column count of matrix A must match row count of matrix B for multiplication).

Calls the appropriate function and displays the result or an error message.












Tools

