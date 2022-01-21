### This is the program of conversion
def Input(list):#for converting other to decimal form
    
    list=[]
    n=int(input("Enter the number of digits:\n"))
    for i in range(n):
        v=str(input("Enter the digits:\n"))
        list.append(v)#Using append for taking input for the list
    print(list)
    
    conv=[]#declaring new list so that reversed list can be stored here
    for j in reversed(list):#operation of conversion takes place from right to left 
        conv.append(j)#reversing list and storing it in new list in reverse order
    # print(conv)
    converted=0
    num=int(input("Choose the base of the digit:\n"))
    for i in range(len(conv)):
        converted+=int(conv[i])*pow(num,i)#for variable powers of the base and adding it
    return converted



def Decimal_Other(list):#converting decimal to other
    list=[]
    number=int(input('Enter the decimal number'))
    n=int(input("Enter the base in which you want to convert the decimal number"))
    while number>1:
        remainder=number%n#for saving the remainder
        number=number/n#for saving the new quotient repeatedly
        list.append(int(remainder))#adding the remainders in the list
        # print(list)
        if(number==1):
           list.append(int(number))#when number becoming 1 we returning 1 to the list
        # print(list)
    new=[]
    for i in reversed(list):
        new.append(i)
    return new
while True:
    key=int(input('''Welcome to the program of conversion\nPress 1 for decimal to other conversion\n2 for other into decimal:\n'''))
    if(key==1):
        print(Decimal_Other(list))#calling function
    elif(key==2):
        print(Input(list))#calling function
    else:
        print("Oops!Invalid input")
    step=int(input("Press any key to continue and 0 for exiting:\n"))
    if(step==0):
        break
