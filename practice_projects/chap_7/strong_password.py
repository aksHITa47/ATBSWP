import re
def strength(pas):
    if len(pas)<8:
        print("Password must contain atleast 8 characters")
    else:
        flag=1
        up=0
        low=0
        dig=0
        for i in range(len(pas)):
            if pas[i].isupper():
                up+=1
            elif pas[i].islower():
                low+=1
            elif pas[i].isdecimal():
                dig+=1
        if low<1:
            flag=0
            print("Password must contain atleast one lowercase alphabet")
        if up<1:
            flag=0
            print("Password must contain atleast one uppercase alphabet")
        if dig<1:
            flag=0
            print("Password must contain atleast one digit")
        return(flag)

ent=str(input("Enter the password: "))
password=ent.strip()
result=strength(password)
if result==1:
    print("Strong password")

# fgs, use regex!

    
