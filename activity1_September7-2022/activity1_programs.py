# Python program to calculate length of a String without using len() function

str = "Python"
print("Given string is = ", str)
length  = 0
for i in str:
    length = length+1
print("Length of string is = ", length)
print()

# Python function to sum all the numbers in a list 

list = [23,45,67,12,9]
print("Given list is = ", list)
sum = 0
for i in list:
    sum = sum+i
print("Sum of numbers = ", sum)
print()

# Finding largest number in a list using sort() method
list1 = [19, 34, 5, 7,1]
print("Given list is = ", list1)
list1.sort()
print("The largest number in the list using sort() = ", list1[-1])
print()

# Finding largest number in a list using max() method
list2 = [5, 18, 3, 99]
print("Given list is = ", list2)
print("The largest number in the list using max() = ", max(list2))
print()

# Write a Python program to print the even numbers from a given list
list3 = [4,7,8,24,33,13]
print("Given list is = ", list3)
print("Even numbers in the list are ...")
for i in list3:
    if i%2 == 0:
        print(i,end =" ")
print()

# --- Samragyi Vats
