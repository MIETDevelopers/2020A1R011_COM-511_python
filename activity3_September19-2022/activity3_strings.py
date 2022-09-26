#Consider the string “Welcome to Python world”. Perform the following operations:

#A. Count the number of alphabets in the given string.

# using isalpha() + len()
print()
print("Count the number of alphabets in the given string")
print("Using isalpha()")
str = "Welcome to Python world"
al = len([ele for ele in str if ele.isalpha()])
print("Number of alphabets: ", al)
print()

#B. To extract characters in the given range from the given string.
print("To extract characters in the given range from the given string")
print("Using join() + list comprehension")
list = ["Welcome", "to", "the", "Python", "world"]
strt, end = 5,20
#res = join([sub for sub in list])[strt:end]
print("Range characters: "+ ' '.join([sub for sub in list])[strt:end])
print()

#C. Check if the string is alphanumeric or not.
print("Check if the string is alphanumeric or not")
print("using isalnum()")
print("The string is: ", str)
print("Is the string alphanumeric? ", str.isalnum())
print()