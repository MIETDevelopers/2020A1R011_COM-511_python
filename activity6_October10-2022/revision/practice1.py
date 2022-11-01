# Perform linear search

def linearSearch(list1, size, key):
    index = -1
    for i in range(0,size):
        if(list1[i]==key):
            index = i
            break
    return index

print("LINEAR SEARCH")
list1 = [12, 34, 15, 6, 89]
size = len(list1)
key = int(input("Enter the element you want to find in the list: "))

result = linearSearch(list1, size, key)
if result == -1:
    print("Element not found at any index")
else:
        print("Element found at index ", result)
print()
"""
index = -1
for i in range(0,size):
    if(list1[i]==key):
        #print("Element found at index ", i)
        index = i
        break;
if index == -1:
    print("Element not found")
else:
    print("Element found at index ", index)
"""    
    
#------------ Samragyi Vats