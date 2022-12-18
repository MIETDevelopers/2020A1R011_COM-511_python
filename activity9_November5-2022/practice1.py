a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

sides = [a,b,c]
x,y,z = sorted(sides)
if x**2 + y**2==z**2:
    print("Right angled triangle")
else:
    print("Not a right angled triangle")
 

s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   