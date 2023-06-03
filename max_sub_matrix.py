def input_matrix(dimen):
    matrix = []

    for i in range(dimen):
        matrix.append([int(i) for i in input().strip().split(" ")])

    return matrix

def sub_matrix(p,matrix):
    sub_matrices = []
    for i in range(p):
        for j in range(p):
            sub_matrix = []
            for k in range(p):
                sub_matrix.append(matrix[i+k][j:j+p])
            sub_matrices.append(sub_matrix)

    return sub_matrices
    
def print_matrix(p,matrix):
    
    for i in range(p):
        for j in range(p):
            print(str(matrix[i][j])+" ",end="")
        print()

def main():
    dimen = int(input("Enter dimentions: "))
    p = 0
    while True:
        p = int(input("Enter p: "))
        if 1<p<dimen:
            break
            
    matrix = input_matrix(dimen)

    max_sub_matrix = max(sub_matrix(p,matrix))

    print_matrix(p,max_sub_matrix)

if __name__=='__main__':
    main()
