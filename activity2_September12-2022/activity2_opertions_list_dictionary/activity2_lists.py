# program to find even numbers from a list

list = [23, 24, 5,12, 4]
print("Even numbers in the list are...")
print()
for i in list:
    if i%2 == 0:
        print(i, end = " ")


#interchange first and last element of a list
print("Given list: ", list)
print("Interchanging first and last elements...")
print()
list[0], list[-1] =list[-1], list[0]
print("List after interchange = ", list)

#merge two lists

list1 = ["Python", "Programming"]
list2 = [3, 24]
#list1.extend(list2)
list3 =(list1 + list2)
print(list3)

# ------ Samragyi Vats
#---------------------------------------------