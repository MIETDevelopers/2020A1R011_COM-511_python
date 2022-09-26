# String Manipulation

# Calculation of length of string

# using len()

str = input("Enter your desired string: ")
print()
length = len(str)
print("Length of the string is : ", length)
print()

# Perform upper case of later part of string

mid = length//2
str1 = str[0:mid]
str2 = str[mid:]
str3 = str2.upper()
#print(str3)
new = str1+str3
print("String after converting the later part to upper case: ", new)
print()


# -Samragyi Vats
#-------------------------------------