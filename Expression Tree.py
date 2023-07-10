class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

    def insert(self,data,bracked=False):

        operator = True if data[0]=="OPERATOR" else False   
        
        node = Node(data)

        #operator & not bracked
        if operator and bracked==False:
            
            pres = {'^':1,'/':2,'*':2,'+':3,'-':4}
            precedence = pres[data[1]]
            
            temp = self
            
            if temp.data[0]=="OPERATOR":
                current_precedence = pres[temp.data[1]]

                if precedence>current_precedence:
                    temp = self.right
                    self.right = node
                    node.left = temp
                else:
                    self = node
                    node.left = temp
            else:
                self = node
                node.left = temp

        
        #operator & bracked
        elif operator and bracked==True:
            temp = self.right
            self.right = node
            node.left = temp


        #operand
        elif not operator:
            temp = self
            
            if temp.right == None:
                temp.right = node
            elif temp.left == None:
                temp.left = node
            else:
                while True:
                    if temp.right.data[0]=="OPERATOR":
                        temp = temp.right
                    elif temp.left.data[0]=="OPERATOR":
                        temp = temp.left
    
                    if temp.left == None:
                        temp.left = node
                        break
                    elif temp.right == None:
                        temp.right = node
                        break

                
        return self


    def tree_visualize(self,level=0):
        if self == None:return
        
        tree_visualize(self.left,level+1)
        print("    "*level+self.data)
        tree.visualize(self.right,level+1)









if __name__=="__main__":        

    root = Node(("OPERAND",1))

    root = root.insert(("OPERATOR",'+'),False)
    root = root.insert(("OPERAND",2),False)
    root = root.insert(("OPERATOR",'*'),True)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'+'),False)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'^'),False)
    root = root.insert(("OPERAND",2),False)

    root.tree_visualize()
