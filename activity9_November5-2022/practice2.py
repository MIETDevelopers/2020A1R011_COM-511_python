start = int(input("Enter start: "))
end = int(input("Enter end: "))
 
# iterating each number in list
for num in range(start, end + 1):
 
    # checking condition
    if num >= 0:
        print(num, end=" ")