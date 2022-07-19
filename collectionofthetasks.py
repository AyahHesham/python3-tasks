class game:
    def __init__(self):
        while True:
            print('''welcome in our game:
            1:listsOfOddAndEven
            2:countsofdistinctwords
            3:listfromzerotolastnumber
            4:Divisiblenumbersinthelist
            5:Divisiblenumbersinthefirstandsecondnum
            6:Exit 
            ''')
            userchoice=input("Enter your choice: ")
            if int(userchoice)==6:
                print("Thank you")
                break
            elif int(userchoice)==1:
                a=int(input("Enter the total numbers of the list: "))
                self.listsOfOddAndEven(a)
            elif int(userchoice)==2:
                words=input("enter your sentance: ")
                self.countsofdistinctwords(words)
            elif int(userchoice)==3:
                lastnum=int(input('enter the last number: '))
                self.listfromzerotolastnumber(lastnum)
            elif int(userchoice)==4:
                firstNum=int(input("Enter the first num: "))
                secondNum=int(input("Enter the second num: "))
                self.Divisiblenumbersinthelist(firstNum,secondNum)
            elif int(userchoice)==5:
                firstNum=int(input("Enter the first num: "))
                secondNum=int(input("Enter the second num: "))
                self.Divisiblenumbersinthefirstandsecondnum(firstNum,secondNum)
            playagain=input("press any key to play again if ypu want to exit presss x:")
            if playagain=='x':
                print("thank you")
                break
       
    def listsOfOddAndEven(self,a):
        list3=[]
        list4=[]
        list5=[]
        for x in range(0,a):
            list3.append(int(input("enter the list items")))
            if x==0 or x%2==0:
                list4.append(x)
            else:
                list5.append(x)
        print(f'the first list is: {list4} and the second list is: {list5}')
    
    def countsofdistinctwords(self,words):
        print(len(set(words.split())))
        
    def listfromzerotolastnumber(self,lastnum):
        for x in range(lastnum+1):
            print(x)
    
    def Divisiblenumbersinthelist(self,firstNum,secondNum):
        for x in range(firstNum):
            if x==0:
                print(x)
                continue       
            if secondNum%x==0:
                print(x)
     
    def Divisiblenumbersinthefirstandsecondnum(self,firstNum,secondNum):
        for x in range(0,101):
            if x==0:
                print(x)
                continue
            if firstNum%x==0 and secondNum%x==0:
                print(x)
game1=game()
