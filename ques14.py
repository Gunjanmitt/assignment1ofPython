def main():
    lines=[]
    while True:
        line=input("enter a line(or press enter to finish):")
        if line==" ":
            break
        lines.append(line)
    print("you entered the following lines:")
    for line in lines:
        print(line)
main()
    