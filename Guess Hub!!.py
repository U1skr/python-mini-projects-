import random as w
def startgame():
    A=[]
    for i in range(97,123):
        A.append(chr(i))
    for i in range(65,91):
        A.append(chr(i))
    print(A)

    cap='A'
    for k in range(66,91):
        cap+=chr(k)
        
    small='a'
    for l in range(98,123):
        small+=chr(l)
    
    count=0
    r=w.choice(A)


    while True:
        count+=1
        inp=input("\n guess the  letter : ")
        if(inp==r):
            print(" \n \"you did it\" ")
            break
            
        if(r in cap):
            if(inp in cap):
                if(ascii(inp)<ascii(r)):
                    print("\n this is too Low")
                else:
                    print("\n this is too High")
                    
            elif(inp in small):
                if(ascii(inp)>ascii(r)):
                    print("\n this is too low")
                else:
                    print("\n this is too high")
        elif(r in small):
            if (inp in cap):
                if(ascii(inp)<ascii(r)):
                    print("\n this is too high")
                else:
                    print("\n this is too low")
            elif(inp in small):
                 if (ascii(inp)>ascii(r)):
                    print("\n this is too high")
                 else:
                    print("\n this is too low")
    return count
c=[]
n=[]
no=int(input("Enter the no of players : "))
for i in range(1,no+1):
    print("\nYour turn,player -",i)
    name=input("Enter your name : ")
    c.append(startgame())
    n.append(name)
print ("\n",c)

print ("\n",n)
print("\n\t\t" ,n[c.index(min(c))],"is the winner!!!$$$ ")
   

