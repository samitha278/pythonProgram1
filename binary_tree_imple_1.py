class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def insert_node(root,node):
    temp = root 

    while temp != None:

        if node.data<temp.data:
            if temp.left==None:
                temp.left = node
                return
            else:
                temp = temp.left
        elif node.data>temp.data:
            if temp.right==None:
                temp.right = node
                return
            else:
                temp = temp.right
        else:
            pass

def create_tree(alist):
    root = Node(alist[0])

    for i in alist[1:]:
        node = Node(i)            
        insert_node(root,node)

    return root 

def main():
    alist = [5,36,8,3,105,20,1,-4,12,15]

    atree = create_tree(alist)

if __name__ == '__main__':
    main()
