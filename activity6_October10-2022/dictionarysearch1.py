students_data = {"Meena" : [55,88,77,66,44],
        "Sumedh":[56,78,55,88,70],
        "Sushil": [44,65,76,33,77]}
print("Original Dictionary : ")
print(students_data)
print()
# searching item in dictionary
name = input("Enter name of student :")
if name in students_data.keys():
    print(students_data[name])
else :
    print("No student found")