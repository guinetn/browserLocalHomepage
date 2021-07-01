## Matrix

matA x matB
matrix multiplication requirements: A no of columns = B no of rows

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]

if len(A[0])==len(B):
    print("\npossible")
else:
    print("\nNot possible")
    print("\for matrix multiplication to be possible no of columns in matrix 1 = no of rows in matrix 2")
    
print("\nEnter The Values in the matrix 1: ")

#"# iterate through A rows
for i in range(len(A)):
    # iterate through B columns
    for j in range(len(B[0])):
        # iterate through rows of 
        for k in range(len(B[0])):
            result[i][j] += A[i][k] * B[k][j]   xy = x k k y
for r in result:
    print(r)

          A        B    =      C
	1 2 3    1 2 3     30  36  42
	4 5 6    4 5 6     66  81  96
	7 8 9    7 8 9     102 126 150
    
