import random as r
rnum=r.randrange(1,100)
count=0
print (rnum)
print("\t \t Welocome to the \"""GUESSING  MASTER \"""\t\t "    )
print("$There will be a number between 1 t0 100 ")
print("$You are going to guess it \n \t\t$$Let's begin$$ !!!\t\t")

while True:
    count+=1
    no=int(input("\n What's your guess  : "))
    if(no==rnum):
        break
    elif(no>rnum):
        print("\n Not that much,go with a \" SMALLER \" digit")
    else:
        print("\n Oh !! this is too small try a \" BIGGER \" one")
              
print("\n Number of guesses : " ,count)
print("\n You found it ",end='\n')
              
if(count<=4 ):
              print("\n Whoaa , you must be a \"genius !!!!\" " )
elif(count<=9):
    print("\n Wow ,That's the  good guess!!")
else:
    print("\n Nice,you guessed it!! ")
    
    
              
