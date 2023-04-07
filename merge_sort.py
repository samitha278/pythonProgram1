def mergeSort(unsort_list):
    length = len(unsort_list)
    
    if(length==1):
        return unsort_list

    left_half = []
    right_half = []    

    half_length = length//2

    for i in range(half_length):
        left_half.append(unsort_list[i])
        right_half.append(unsort_list[i+half_length])

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    sorted_list = merge(half_length,left_half,right_half)

    return sorted_list


def merge(length,left_half,right_half):

    merge_list = []

    i = 0;j= 0; 
    while (i<length and j<length):
        if(left_half[i]<right_half[j]):
            merge_list.append(left_half[i])
            i+=1
        elif(right_half[j]<left_half[i]):
            merge_list.append(right_half[j])
            j+=1
    if(i>=length):
        list = [i for i in right_half[j:]]
        merge_list+=list
    if(j>=length):
        list = [i for i in left_half[i:]]
        merge_list+=list

    return merge_list


def main():
    unsort_list = [1,4,2,3,8,7,9,5,6,10]

    sorted_list = mergeSort(unsort_list)

    print(sorted_list)


if __name__ == '__main__':
    main()
