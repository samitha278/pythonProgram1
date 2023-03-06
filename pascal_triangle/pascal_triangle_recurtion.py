class Pascal(object): 
    def genarate(self,numRows):
        return genarate_pascal(numRows)
        
def genarate_pascal(numRows):
    if(numRows==1):
            return [[1]]
    
    pascal = genarate_pascal(numRows-1)
        
    i = 1
    row = [1]
    while(i<numRows):
        if i == numRows-1:
            row.append(1)
        else:
            row.append(pascal[i][i-1]+pascal[i][i])
            
        i+=1
            
    pascal.append(row)
    return pascal

def main():
    pascal = Pascal()
    print(pascal.genarate(5))

if __name__ == '__main__':
    main()
