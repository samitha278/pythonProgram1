def print_matrix(matrix):
    '''print matrix '''
    
    #check empty matrix
    if matrix == None :
        return f"Error"
        
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(rows):
        for j in range(columns):
            print(f"{matrix[i][j]} ",end="")
        print()
    
    return 0   


def transpose_matrix(matrix):
    '''get matrix as argument & return its transpose matrix'''
    
    #find number of rows and columns
    rows = len(matrix)
    columns = len(matrix[0])
    
    #create transpose matrix by columns into rows
    t_matrix = []
    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        t_matrix.append(row)

    return t_matrix
    

def get_row():
    row_str = input().strip()
    
    #check -1,stop accepting the rows when -1 is entered as the input    
    if row_str =='-1':
        return -1
        
    # convert the input string to a list of integers
    try:
        row = list(map(int,row_str.split()))
    except ValueError:
        print("Error")
        return -2
        
    return row
        
    
def get_matrix():
    '''get matrix from user as input & store in it as 2D array'''
    
    matrix = []
    
    #create 1st row and append it to matrix 2D list        
    row_1 = get_row()
    if row_1 == -1 or row_1 == -2:
        return -2
        
    matrix.append(row_1)
    columns = len(row_1)
     
    #input multiple lines  
    while True:
        row = get_row()
        
        #break oop when row equal to -1
        if row==-1:
            break
        elif row==-2:
            return -2
        
        #check invalid row with an inconsistent number of elements
        if len(row)==columns:
            matrix.append(row)
        else:
            print("Invalid Matrix")
            return -2
        
    return matrix
    

def main():
    #input matrix
    matrix = get_matrix()
    
    #exceptions
    if matrix == -2 :
        return -2
    
    #get transpose matrix
    t_matrix = transpose_matrix(matrix)
    
    #print matrix
    print_matrix(t_matrix)
    
    return 0
    
if __name__=='__main__':
    main()
