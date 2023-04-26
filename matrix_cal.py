def get_matrix(rows,columns):
	'''get matrix from user as input &
	store in it as 2D array'''
    
    matrix = []
    for row in range(rows):
        get_row = input(f"    {row+1} row's {columns} elements: ").strip().split(" ")
        row = []
        for element in get_row:
            row.append(int(element))
        matrix.append(row)

    return matrix
 
def transpose_matrix(matrix,rows,columns):
	'''get matrix as argument & return its 
	transpose matrix'''

    t_matrix = []
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        t_matrix.append(row)

    return t_matrix


def matrix_multiplier(matA,matB):
	'''get 2 matix as argument & return 
	multiply of these matriseas'''
    
    if len(matA[0]) != len(matB):
        return f"can't multiply matrices"
    
    matrix_mul = []
    
    m = len(matA)
    n = len(matB[0])

    for i in range(m):
        row = []
        for j in range(n):
            asum = 0
            for k in range(len(matB)):
                asum += (matA[i][k]*matB[k][j])
            row.append(asum)
        matrix_mul.append(row)

    return matrix_mul
    
def print_matrix(matrix):
    '''print matrix '''
    if matrix == None :
        return f"empty matrix"
        
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(rows):
        for j in range(columns):
            print(f"    {matrix[i][j]}",end= " ")
        print()
        
def main():
    #get matrix A
    print("Enter matrix A #rows & #columns: ")
    rowA = int(input("#rows: "))
    columnA = int(input("#columns: "))
    A = get_matrix(rowA,columnA)
    
    #get matrix B    
    print("Enter matrix B #rows & #columns: ")
    rowB = int(input("#rows: "))
    columnB = int(input("#columns: "))
    B = get_matrix(rowB,columnB)

    B_T = transpose_matrix(B,rowB,columnB)

    print("matrix A * transpose matrix B")
    print_matrix(matrix_multiplier(A,B_T))

if __name__ == '__main__':
    main()
