
list3=[]
list4=[]
list5=[]
a=int(input('enter the total numbers of the list'))
for x in range(a):
    list3.append(input("enter the list items"))
    if x==0 or x%2==0:
        list4.append(x)
    else:
        list5.append(x)
print(f'the first list is: {list4} and the second list is: {list5}')

