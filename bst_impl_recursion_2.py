#define Node class
class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def insert(root,data):
	'''insert new data to tree using recursion method'''
	
	#check if root is NULL
    if (root == None):
        root = Node(data)

    #new data is lesser than root's data,
    #then data insert to left sub-tree     
    elif (data<=root.data):
        root.left = insert(root.left,data)
    
    #new data is greater than root's data,
    #then data insert to right sub-tree
    else:
        root.right = insert(root.right,data)

    return root

def search(root,data)->bool:
    '''search data through tree using recursion method'''
    
    #data not in tree,
    #then return false after go through full tree 
    if (root == None):
        return False
    #return when data found
    elif (root.data == data):
        return True

    #root data not equal to data,
    #then search through left-sub tree
    elif (data<=root.data):
        abool = search(root.left,data)

    #root data not equal to data,
    #then search through right-sub tree
    else:
        abool = search(root.right,data)
    
    return abool

#main function
def main():
    alist = [5,36,8,3,105,20,1,-4,12,15]
    root = None

    for i in alist:
        root = insert(root,i)
        
    print(search(root,12))
    print(search(root,112))

if __name__ == '__main__':
    main()
