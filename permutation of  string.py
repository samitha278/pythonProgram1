def permu(st, const = ""):
    
    n = len(st)
    
    #base case
    if n == 1 or n==0:
        print(const+st)
        return  
    
    list = []
    for ch in st:
        list.append(ch)
    
    for i in range(n):
        new_const = const
        next_permu = ""
        for j in range(n):
            if list[i]==list[j]:
                new_const += list[i]
            else:
                next_permu += list[j]

        #recursive case        
        permutation_name = permu(next_permu,new_const)  
        
    return 
      

def main():
    permu("ABCD")

if __name__ == '__main__':
    main()
