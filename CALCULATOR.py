#create a simple claculator using python 
#step 1: define the functions of the file
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1 / num2

def average(num1,num2):
    return (num1+num2)/2

def raise_to_power(num1,num2):
    return num1**num2

print("please select the operation:")
print("1.Addition")
print("2.Substraction")
print("3.Multiply")
print("4.Division")
print("5.Average")
print("6.Power")
while True:
    select = int(input("Please select the operation from 1,2,3,4,5: "))
    

    number1= int(input("Enter a number1:"))
    number2= int(input("Enter a number2: "))
    if select==1:
        print("Addition of two numbers is equal to : ")
        print(number1, "+", number2 ,"=", add(number1,number2))

    elif select==2:
        print("Substraction of two numbers is equal to : ")
        print(number1,"-",number2,"=", sub(number1,number2))

    elif select==3:
        print("Multiplication of two numbers is equal to : ")
        print(number1,"*",number2,multiply(number1,number2))

    elif select==4:
        print("Division of two numbers is equal to : ")
        print(number1,"/",number2,divide(number1,number2))

    elif select==5:
        print("Average of two numbers is equal to : ")
        print("(",number1,"+",number2,")","/","2","=",average(number1,number2))

    elif select==6:
        print("Power of a number is equal to : ")
        print(number1,"^",number2,"=",raise_to_power(number1,number2))

    else:
        print("invalid operation , please try again!")
    print("ENTER y TO CONTINUE \n ENTER n to BREAK")
    op=input("DO YOU WANT TO PERFORM MORE OPERATION : ")
    if op=='n':
        print("THANK YOU FOR USING CALCULATOR:")
        break