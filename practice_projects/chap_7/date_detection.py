import re
# How cool is the name valiDate!?
def valiDate(stringl):
    date,month,year=stringl.groups()
    months_30=['04','06','09','11']
    months_31=['01','03','05','07','08','10','12']
    if int(month)>12:
        print("There are 12 months in a year")
    else:
        if month=='02':
            lp=int(year)
            if lp%4==0:
                if lp%100==0:                
                    if lp%400==0:
                        if int(date)<=29:
                            print("Valid Date")
                        else:
                            print("Date exceeded")
                if int(date)<=29:
                    print("Valid Date")
                else:
                    print("Date Exceeded")
            else:
                if int(date)<=28:
                    print("Valid Date")
                else:
                    print("Date exceeded")
        for i in range(len(months_30)):
            if month==months_30[i]:
                if int(date)<=30:
                    print("Valid Date")
                else:
                    print("Date exceeded")
        for i in range(len(months_31)):
            if month==months_31[i]:
                if int(date)<=31:
                    print("Valid Date")
                else:
                    print("Date exceeded")
date=str(input("Enter date in DD/MM/YYYY format: "))
dateRegex=re.compile(r'(\d{2})/(\d{2})/(\d{4})')
ext=dateRegex.search(date)
if ext==None:
    print("Invalid Date format")
#date,month,year=ext.groups()
else:
    valiDate(ext)
