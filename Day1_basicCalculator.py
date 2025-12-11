num1 = float(input("Enter no 1 : ")
num2 = float(input("Enter no 2 : ")

print("choose operator")

print("1 choose + ")
print("2 choose -")
print("3 choose *")
print("4 choose / ")

choose = int(input(" choose 1/2/3/4 ")

if choose==1:
    result = num1 + num2
    print(result)
elif choose==2:
    result = num1 - num2
    print(result)
elif choose==3:
    result = num1 * num2
    print(result)
else choose==4:
    result = num1 /num2
    print(result)
else:
    print("you have enter wrong choose" , "re enter the thing ")
