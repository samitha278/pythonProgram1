class Pascal(object): 
        
    def genarate_pascal(self,numRows):
        if(numRows==1):
            return [[1]]
        
        
        pascal = self.genarate_pascal(numRows-1)
            
        i = 1
        j = numRows-2
        row = [1]
        
        while(i<numRows):
            if i == numRows-1:
                row.append(1)
            else:
                row.append(pascal[j][i-1]+pascal[j][i])
                
            i+=1
                
        pascal.append(row)
        return pascal

def main():
    pascal = Pascal()
    print(pascal.genarate_pascal(5))

if __name__ == '__main__':
    main()
