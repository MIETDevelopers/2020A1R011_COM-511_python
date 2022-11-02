#program to find if a given number is armstrong or not

def isArmstrong(x):
    
    n = order(x)
    temp = x
    sum1 = 0
    
    while temp!=0:
        r = temp % 10
        sum1 = sum1 + pow(r, 3)  #using the pow() function to calculate the cube
        temp = temp//10
        
    return (sum1 == x)

def order(x):
    
    n = 0
    while x!=0:
        n = n+1
        x = x//10
    
    return n

# input number which you want to check
x = int(input("Enter a number: "))
print(isArmstrong(x))