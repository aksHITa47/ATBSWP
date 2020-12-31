def comma(para):
    s=''
    if len(para)!=0:
        for i in range(len(para)-1):
            s= s+str(str(para[i])+', ')
        s=s+ str('and' + ' '+ str(para[-1]))
    print(s)

a=[]
while True:
    print("Enter the "+ str(len(a)+1) +' value (or hit enter to stop adding values in list)')
    item=input()
    if item=='':
        break
    else:
        a.append(item)
comma(a)

# Do something for empty list and single valued list
        



