class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

    def insert(self,data,bracketed):

        operator = True if data[0]=="OPERATOR" else False   
        node = Node(data)

        #operator
        if operator: 
            if bracketed:
                temp = self.right
                self.right = node
                node.left = temp
            else:
            
                pres = {'^':4,'/':3,'*':3,'+':2,'-':2}
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


    def evaluate(self):
        
        operand = True if self.data[0]=="OPERAND" else False
        
        if operand:
            return self.data[1]
        
        operator = self.data[1]
        left = self.left
        right = self.right
        
        match operator:
            case '+':
                value = right.evaluate()+left.evaluate()
                print("+",value)
                return value
            case '-':
                value = right.evaluate()-left.evaluate()
                print("-",value)
                return value
            case '*':
                value = right.evaluate()*left.evaluate()
                print("*",value)
                return value
            case '/':
                value = right.evaluate()/left.evaluate()
                print("/",value)
                return value
            case '^':
                value = left.evaluate()**right.evaluate()
                print("^",value)
                return value
            case '_':
                return



    def tree_vis(self,level=0):
        if self.left == None or self.right == None:
            print('        '*level , f"{self.data}")
            return 

        left = self.left
        right = self.right
        
        right.tree_vis(level+1)
        print('        '*level , f"{self.data}")
        left.tree_vis(level+1)










def test1():
    root = Node(("OPERAND",1))

    root = root.insert(("OPERATOR",'+'),False)
    root = root.insert(("OPERAND",2),False)
    root = root.insert(("OPERATOR",'*'),True)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'+'),False)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'^'),False)
    root = root.insert(("OPERAND",2),False)

    result = root.evaluate()
    print(result)
    root.tree_vis()


def test2():
    root = Node(("OPERAND",1))

    root = root.insert(("OPERATOR",'+'),False)
    root = root.insert(("OPERAND",2),False)
    root = root.insert(("OPERATOR",'*'),True)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'+'),True)
    root = root.insert(("OPERAND",3),False)
    root = root.insert(("OPERATOR",'^'),False)
    root = root.insert(("OPERAND",2),False)

    result = root.evaluate()
    print(result)
    root.tree_vis()

def test3():
    root = Node(("OPERAND",-15))

    root = root.insert(("OPERATOR",'-'),False)
    root = root.insert(("OPERAND",99),False)
    root = root.insert(("OPERATOR",'*'),True)
    root = root.insert(("OPERAND",10),False)

    result = root.evaluate()
    print(result)
    root.tree_vis()



if __name__=="__main__":        
    test1()
'''
    print("\n\n\n\n")
    test2()
    print("\n\n\n\n")
    test3()
'''
    
    
