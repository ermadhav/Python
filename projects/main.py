try:
    a = int(input("Enter the first num: "))
    b = int(input("Enter the first num: "))

    print("What kind of operation you want to perform : +,-,*,/ ")
    o = input("Enter operation: ")
    match o: 
        case "+":
            print(f"result = {a+b}")
        case "-":
            print(f"result = {a-b}")
        case "*":
            print(f"result = {a*b}")
        case "/":
            print(f"result = {a/b}")    

except Exception as e:
    print("enter a valid value of a and b")        