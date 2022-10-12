# linear search in python

# function for linear search
def linearSearch(list, n, key):
    for i in range(0,n):
        if(list[i]==key):
            return i
        return -1
print("Linear Search in Python")
list1 = [1,3,4,6,12,45]
key = int(input("Enter the element you want to search: "))
n = len(list1)
ret = linearSearch(list1, n, key)
if(ret == -1):
    print("Element not found at any index.")
else:
    print("Element found at index ", ret)
print()    

# Binary Search in Python
# iterative method
print("Binary Search in python")
def binarySearch(list, n):
    low = 0
    high = len(list) - 1
    mid = 0
    while low <= high:
        mid = (high+low)//2
        if list[mid]<n:
            low = mid+1
        elif list[mid] >n:
            high = mid - 1
        else:
            return mid
        return -1
    
list1 = [12, 23, 3, 45, 67]
n = 45
result = binarySearch(list1, n)
if result != -1:
    print("Element found at index ", result)
else:
    print("Element not found") 
print()       


# Samragyi Vats
#-----------------------------