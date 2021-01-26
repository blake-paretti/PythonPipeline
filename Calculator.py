def add(a, b):
    return str(a+b)

def sub(a, b):
    return str(a-b)

def divide(a, b):
    return str(a/b)

def mult(a, b):
    return str(a*b)

def takeNum1():
    print("What numbers whould you like to " + string + "?")
    print("")
    print("Input first number:")
    print("")
    return input()
def takeNum2():
    print("")
    print("Input second number:")
    print("")
    return input()

global running
global userIn
global string

running = True
while(running):
    print("What would you like to do?")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    print("")
    print("")
    userIn = input()
    print("")
    print("")
    string = ""
    if(userIn == "1"):
        string = "add"
        a = takeNum1()
        b = takeNum2()
        answ = add(int(a), int(b))
        print("")
        print("")
        print(a + " + " + str(b) + " = " + answ)
    elif(userIn == "2"):
        string = "subtract"
        a = takeNum1()
        b = takeNum2()
        answ = sub(int(a), int(b))
        print("")
        print("")
        print(a + " - " + b + " = " + answ)
    elif(userIn == "3"):
        string = "multiply"
        a = takeNum1()
        b = takeNum2()
        answ = mult(int(a), int(b))
        print("")
        print("")
        print(a + " x " + b + " = " + answ)
    elif(userIn == "4"):
        string = "divide"
        a = takeNum1()
        b = takeNum2()
        answ = divide(int(a), int(b))
        print("")
        print("")
        print(a + " / " + b + " = " + answ)
    elif(userIn == "5"):
        running = False
    print("")
    print("")
    print("")
    
