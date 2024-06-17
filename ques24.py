def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return  x*y
def divide(x,y):
    if y==0:
        return "error by zero division"
    else:
        return x/y
def calculator():
    print("select operation:")
    print("1.Adittion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice=input("enter your choice(1/2/3/4):")
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
    
