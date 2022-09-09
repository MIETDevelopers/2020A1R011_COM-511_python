# Write a program to demonstrate type checking of various data types and demonstrate the
#use of following built in functions in python: abs(), len(), min(), round(), isalnum(), type().


# -----------------------------------------------------
# TYPE CHECKING OF VARIOUS DATA TYPES

#let us consider the following variables 

# Python numbers

a = 10
b =20.5
c = 2+4j

#checking the data types for a,b and c

print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is of type", type(c))

# Python List

lis = [2, 3, "python", 1+24j]

# checking the data type of lis

print(lis, "is of type", type(lis))

# Python tuple

tup = (34, "coding is fun")

# checking the data type of tup

print(tup, "is of type", type(tup))

# Python String

str = "This is a Python Code"

# checking the data type of str

print(str, "is of type", type(str))

# Python set

s = {1,2,3,4,5}

# checking the data type for s

print(s, "is of type", type(s))

# Python Dictionary

dict = {"animal": "rabbit", "fruit": "orange"}

# checking the data type for dict

print(dict, "is of type", type(dict))
print()

#----------------------------------------------------------------


# BUILT IN FUNCTIONS OF PYTHON

# abs()

number = -20
absolute_number = abs(number)
print("Use of abs() function")
print("Given number = ", number)
print("Absolute value = ",absolute_number)
print()

# len()

colors = ['red', 'blue', 'green']
print("Use of len()")
print("Given list = ", colors)
print("Length = ", len(colors))
print()

#min()

num = [43,12,3,7]
print("Use of min()")
print("Given list = ", num)
print("Minimum value = ", min(num))
print()

#round()

print("Use of round()")
n = 34.5
print("Given number = ", n)
print("Round off = ", round(n))
print()

# isalnum()
print("Use of isalnum()")
name1 = "Python3"
print("Given string = ", name1)
print("Alphanumeric?" ,name1.isalnum())
name2 = "Python 3"
print("Given string = ", name2)
print("Alphanumeric?",name2.isalnum())
print()

# type()

print("Use of type()")
numb = 23.54
print("Given variable = ", numb)
print("Type of variable = ", type(numb))
print()

#--------------------------------------------------------
