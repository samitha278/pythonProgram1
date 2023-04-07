#merge sort function
def mergeSort(unsort_list):
    length = len(unsort_list)
    
    #base case
    if(length==1):
        return unsort_list
    
    #create left half & right half
    left_half = []
    right_half = []    

    half_length = length//2

    for i in range(half_length):
        left_half.append(unsort_list[i])
        right_half.append(unsort_list[i+half_length])
    if(length%2==1):
        right_half.append(unsort_list[-1])
    
    #recursive case
    if(len(left_half)==2):
        if(left_half[0]<left_half[1]):
            right_half = mergeSort(right_half)
        else:
            left_half = mergeSort(left_half)
    elif(len(right_half)==2):
        if(right_half[0]<right_half[1]):
            left_half = mergeSort(left_half)
        else:
            right_half = mergeSort(right_half)
    else:
        #recursive case(main)
        left_half = mergeSort(left_half)
        right_half = mergeSort(right_half)

    #call merge function    
    sorted_list = merge(left_half,right_half)

    return sorted_list

#merge function
def merge(left_half,right_half):

    merge_list = []
    
    len_lh = len(left_half)
    len_rh = len(right_half)
    
    i = 0;j= 0; 
    
    while (i<len_lh and j<len_rh):
        if(left_half[i]<right_half[j]):
            merge_list.append(left_half[i])
            i+=1
        elif(right_half[j]<left_half[i]):
            merge_list.append(right_half[j])
            j+=1
    if(i>=len_lh):
        list = [i for i in right_half[j:]]
        merge_list+=list
    if(j>=len_rh):
        list = [i for i in left_half[i:]]
        merge_list+=list

    return merge_list


def main():
    unsort_list = [1,10,4,2,9,3,8,7,5,6]
    
    #call merge sort function
    sorted_list = mergeSort(unsort_list)

    print(sorted_list)


if __name__ == '__main__':
    main()
