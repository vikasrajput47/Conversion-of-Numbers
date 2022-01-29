import random 
win=0
loose=0
attempt=0
mylist=["Stone","Paper","Scissor"]
computer=random.choice(mylist)
print("Welcome to the game there will be five round person who win 3 round is declared as winner")
while True:
    computer=random.choice(mylist)
    # print(computer)
    n=input('Stone ,Paper or Scissor\n')
    if(computer=="Stone"):
        if(n=="Paper"):
            print("Win\n")
            win+=1
        elif(n=="Scissor"):
            print("Loose\n")
            loose+=1
        else:
            print("Draw\n")
    elif(computer=="Paper"):
        if(n=="Scissor"):
            print("Win\n")
            win+=1
        elif(n=="Stone"):
            print("loose\n")
            loose+=1
        else:
            print("Draw\n")
    elif(computer=="Scissor"):
        if(n=="Paper"):
            print("Loose\n")
            loose+=1
        elif(n=="Stone"):
            print("Win\n")
            win+=1
        else:
            print("Draw\n")
    else:
        print(f'wrong input\n')
    attempt+=1
    if(attempt>=5):
        if(win>=3):
            print("You won\n",win,'is your score')
        elif(loose>=3):
            print("You loose\n",loose,'is your score')
        else:
            print("Draw",win,'is your score')
        v=int(input("Enter 0 for exit or any other for continue"))
        if(v==0):
            break
        
