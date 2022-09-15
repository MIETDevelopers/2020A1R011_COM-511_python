#Write a python script to check whether a given key already exists or not

fruits = {1: "Apple", 2: "Mango", 3: "Orange", 4: "Grapes"}
print("The dictionary is ...\n")
print(fruits)
findKey = int(input("Enter the key value you want to find "))
for i in fruits:
    if findKey in fruits:
        print("The key exists")
        break
    else:
        print("The key does not exist")
        break
print()

# merge two dictionaries
print("Merging dictionaries\n")
moreFruits = {5: "Banana", 6:"Kiwi"}
moreFruits.update(fruits)
print("Merged dictionary is...\n")
print(moreFruits)

# ------ Samragyi Vats
#---------------------------------------------