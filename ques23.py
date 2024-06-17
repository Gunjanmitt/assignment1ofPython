def celsius_to_fahrenheit(celsius):
    return (celsius*9/5)+32
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32)*5/9
def main():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1 or 2):"))

    if choice==1:
        celsius=float(input("enter temp in celsius:"))
        fahrenheit=celsius_to_fahrenheit(celsius)
        print("temperature in fahrenheit:",fahrenheit)
    elif choice==2:
        fahrenheit=float(input("enter temp in fahrenheit:"))
        celsius=fahrenheit_to_celsius(fahrenheit)
        print("temp in celsius:",celsius)
    else:
        print("invalid choice")
main()    