class Solution: 

    def numSquares(self,n:int) -> int:

        SqrList = [i**2 for i in range(1,int((n**0.5)+1))]
        SqrList.sort(reverse=True)
        numSqrList = []

        for j in range(len(SqrList)):
            if SqrList[j]==1:
                break
            x = n - SqrList[j]
            numPerSqr = 1

            while x != 0 :
                if x in SqrList:
                    numPerSqr+=1
                    break
                else:
                    if(x < 4):
                        numPerSqr+=x
                        break
                    else:
                        for k in SqrList:
                            if k<x:
                                x = x - k
                                break
                        numPerSqr +=1
                        
            numSqrList.append(numPerSqr)

        return min(numSqrList)

def main():
    x = Solution()
    y = x.numSquares(int(input("Enter: ")))
    print(y)

if __name__ == '__main__':
    main()
