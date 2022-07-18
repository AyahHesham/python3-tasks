firstNum=int(input("Enter the first num: "))
secondNum=int(input("Enter the second num: "))
for x in range(0,101):
    if x==0:
        print(x)
        continue
    if firstNum%x==0 and secondNum%x==0:
        print(x)
        