def addition(num1, num2):
    num1 += num2
    return num1
def subtraction(num1, num2):
    num1 -= num2
    return num1
def mul(num1, num2):
    num1 *= num2
    return num1
def division(num1, num2):
    num1 /= num2
    return num1
def module(num1, num2):
    num1 %= num2
    return num1
def default(num1, num2):
    return "Incorrect input"
switcher = {
1: addition,
2: subtraction,
3: mul,
4: division,
5: module
}
def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)

print("Operations \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Module ")
# Take input from user
choice = int(input("Select operation from 1,2,3,4 : "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print (switch(choice, num1, num2))