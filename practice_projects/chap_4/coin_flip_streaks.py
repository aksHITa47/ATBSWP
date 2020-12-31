import random
numberOfStreaks = 0
streak=0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.

    list_1=[]
    for i in range(100):
        r=random.randint(0,1)
        if r==0:
            list_1.append('H')
        elif r==1:
            list_1.append('T')
    
    # Code that checks if there is a streak of 6 heads or tails in a row.

    for i in range(1,len(list_1)):
        if list_1[i-1] == list_1[i]:  
            streak += 1 
        else:
            streak = 0

        if streak == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks /10000))