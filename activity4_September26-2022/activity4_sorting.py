# bubble sort

def bubblesort(list):
    # Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
list = [19,2,31,45,6,11,121,27]
print("List before bubble sort...")
print(list)
bubblesort(list)
print("List after bubble sort...")
print(list)
print()


# insertion sort

def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element
list1 = [12,2,34,5, 15, 56,7]
print("List before insertion sort...")
print(list1)
insertion_sort(list1)
print("List after insertion sort...")
print(list1)
print()

# merge sort


def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return (merge(left_list, right_list))

# Merge the sorted halves
def merge(left_half,right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("List before merge sort...")
print(unsorted_list)
print("List after merge sort...")
print(merge_sort(unsorted_list))
print()

# selection sort

def selectionSort(list2, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if list2[j] < list2[min_index]:
                min_index = j
         # swapping the elements to sort
        (list2[ind], list2[min_index]) = (list2[min_index], list2[ind])
 
list2 = [45, 0, 11, 88,747]
size = len(list2)
print("List before selection sort...")
print(list2)
selectionSort(list2, size)
print("List after selection sort...")
print(list2)
print()

# Samragyi Vats
# -----------------------------------