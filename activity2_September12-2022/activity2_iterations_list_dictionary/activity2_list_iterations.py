# Write a program to illustrate iteration over the list

#--------------------------------FOR LISTS--------------------------

print("ITERATIONS IN LISTS")

# using for loop
print("iteration using for loop")
list = [2,3,4,5]
for i in list:
    print(i)
    
# using for loop and range()
print()
print("iteration using for loop and range()")
length = len(list)
for i in range(length):
    print(list[i])
print()

# using while loop
print("iteration using while loop")
i = 0
while i<length:
    print(list[i])
    i = i+1
print()

# using list comprehension  
[print(i) for i in list]
print()


# ------ Samragyi Vats
#---------------------------------------------