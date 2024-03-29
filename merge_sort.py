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
        if(left_half[i]<=right_half[j]):
            merge_list.append(left_half[i])
            i+=1
        elif(right_half[j]<=left_half[i]):
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
    unsort_list = [567,1,10,11,-23,278,-9876,2,67,567,88,-3,9,15,-3,65,8,7,143,6843,5,-467,6]
    
    #call merge sort function
    sorted_list = mergeSort(unsort_list)

    print(sorted_list)


if __name__ == '__main__':
    main()
