# Program to find the largest number



def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

print("creating a function maximum()")
a = int(input("Enter first number "))
b = int(input("Enter second number "))
c = int(input("Enter third number "))
print("Maximum number is: ", maximum(a, b, c))
print()



def maxi(p,q,r):
    list = [p,q,r]
    return max(list)

print("Using list and max() function")
p = int(input("Enter first number "))
q = int(input("Enter second number "))
r = int(input("Enter third number "))
print("Maximum number is: ", maxi(p,q,r))
print()


print("Using in-built max() function")
x = int(input("Enter first number "))
y = int(input("Enter second number "))
z = int(input("Enter third number "))
print("Maximum number is: ", max(x,y,z))
print()


# -------------------------- SAMRAGYI VATS---------------------------