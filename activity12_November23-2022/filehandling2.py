f = open("exp.txt", "w")
a = input("Enter the line : \n")
b = input("Enter the line : \n")
c = input("Enter the line : \n")
new_line = "\n"
f.write(a)
f.write(new_line)
f.write(b)
f.write(new_line)
f.write(c)
print("\n")
f = open("exp.txt", "r")
print(f.read())
