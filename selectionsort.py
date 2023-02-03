a_list = [4, 1, 5, 3, 2]

def selectionsort(unsorted_List):
    print(unsorted_List)
    for i in range(len(unsorted_List)):
        smallest_index = i
        for j in range(i + 1, len(unsorted_List)):
            if unsorted_List[j] < unsorted_List[smallest_index]:
                smallest_index = j
        unsorted_List[smallest_index], unsorted_List[i] = unsorted_List[i], unsorted_List[smallest_index]
    print(unsorted_List)

selectionsort(a_list)

'''
insertion sort
bubble sort 
merge sort 
quick sort 
'''