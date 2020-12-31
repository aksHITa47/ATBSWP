import re
# How cool is the name valiDate!?
def valiDate(stringl):
    date,month,year=stringl.groups()
    months_30=['04','06','09','11']
    months_31=['01','03','05','07','08','10','12']
    feb='02'
    flag=1
    if month==feb:
        lp=int(year)
        if lp%4==0 and lp%100!=0:
            if int(date)<=29:
                return(flag)
            else:
                flag=0
        else:
            if int(date)<=28:
                return(flag)
            else:
                flag=0
    for i in range(len(months_30)):
        if month==months_30[i]:
            if int(date)<=30:
                return(flag)
            else:
                flag=0
    for i in range(len(months_31)):
        if month==months_31[i]:
            if int(date)<=31:
                return(flag)
            else:
                flag=0
    return(flag)
date=str(input("Enter date in DD/MM/YYYY format: "))
dateRegex=re.compile(r'(\d{2})/(\d{2})/(\d{4})')
ext=dateRegex.search(date)
#date,month,year=ext.groups()
valid=valiDate(ext)
#print(ext)
if valid==1:
    print("The entered date is valid")
elif valid==0:
    print("The date entered is invalid")