def sqr(x):
    
    start = 0
    end = x//2
    
    while (start <= end) :
        middle = (start + end)//2
        n = middle*middle
        if(n==x):
            return middle 
        elif(n<x):
            start = middle + 1
        elif(n>x):
            end = middle - 1
        
    for i in frange(end,start,0.01):
        middle = (start + end)/2
        n = middle*middle
        if(n==x):
            return middle 
        elif(n<x):
            start = middle + 1
        elif(n>x):
            end = middle - 1
    
    return "between "+str(end)+" "+str(start)
    
def main():
    while True:
        print(sqr(int(input("Enter: "))))


if __name__ == '__main__':
    main()
