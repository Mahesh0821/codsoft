num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
print("select your opteration")
print("+ - * / %")
opt=input()
if opt=="+":
    print("sum = ",num1+num2)
elif opt=="-":
    print("difference = ",num1-num2)
elif opt=="*":
    print("product = ",num1*num2)
elif opt=="/":
    print("product = ",num1/num2)
elif opt=="%":
    print("remainder = ",num1%num2)
else:
    print("invalid operation")
