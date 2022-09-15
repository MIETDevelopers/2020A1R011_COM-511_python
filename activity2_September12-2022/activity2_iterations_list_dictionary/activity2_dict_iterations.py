# Write a program to illustrate iteration over dictionary
# ------------------------------------FOR DICTIONARY----------------------

print("ITERATIONS IN DICTIONARY")

dict = {1: "one", 2: "Two", 3: "Three"}

# Access key using the build.keys()
print("Using build.keys()")
keys  = dict.keys()
print(keys)
print()

# Access key without using a key()
print("Without using key()")
print("Iteration over keys")

for i in dict:
    print(i)
    
print()

# iteration through all values using .values()

print("Iteration through values")
for j in dict.values():
    print(j)
print()

# iteration through all keys and value pairs using .items()
print("Iteration using items()")
for i, j in dict.items():
    print(i," : ", j)
print()

# Access both key and value without using items()
print("Iterations without using items()")
for k in dict:
    print(k, '->', dict[k])
print()

# print items in key-value in pair
pair = dict.items()
print(pair)
print()

# ------ Samragyi Vats
#---------------------------------------------