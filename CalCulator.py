
def add(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",substraction(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=",multiplication(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",division(num1,num2))
else:
    print("please enter valid choice")

