import calc as c


while True :
    command = input("required operation : add,sub,mult,div ")
    num1 = int(input("first num :"))
    num2 = int(input("srcond num :"))
    if command == "add":
        out = c.add(num1,num2)
        print (out)
    elif command == "sub":
        out = c.sub(num1,num2)
        print(out)
    elif command == "mult":
        out = c.sub(num1,num2)
        print(out)
    elif command == "div":
        out = c.sub(num1,num2)
        print(out)
    else:
        print(" Error in command ")
    
    check = input("Do you want to continue ? yes / stop")
    if check == "yes":
        continue
    else:
        break
    

