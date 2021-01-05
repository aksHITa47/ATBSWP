import pyinputplus as pyp 

def order():
    bill=0
    bl=['White','Brown','Sourdough']
    pr=['chicken','turkey','ham','tofu']
    bp={bl[0]:1,bl[1]:2,bl[2]:3}
    prop={pr[0]:4,pr[1]:5,pr[2]:6,pr[3]:7}
    #bl= ['White', 'Brown', 'Sourdough']
    bread = pyp.inputMenu(bl,prompt = 'What type of bread would you like?\n',numbered=True)
    #bread=pyp.inputMenu(bl,numbered=True)
    bill+=bp[bread]
    pro=pyp.inputMenu(pr,numbered=True,prompt="What protein source would you like?\n")
    bill+=prop[pro]
    
    chew=pyp.inputYesNo(prompt="Do you want cheese?\n")
    if chew=='yes':
        chee=['cheddar', 'Swiss', 'mozzarella']
        chp={chee[0]:10,chee[1]:11,chee[2]:12}
        cheese=pyp.inputMenu(chee,prompt="What kinda cheese do you want?\n",numbered=True)
        bill+=chp[cheese]
    else:
        print("Healthy choice!")

    add=pyp.inputYesNo(prompt="Do you want mayo, mustard, lettuce, or tomato?\n")
    if add=='yes':
        adds={'mayo':13,'mustard':14,'lettuce':15,'tomato':16}
        added=pyp.inputMenu(list(adds.keys()),prompt="What extras do you wanna add?\n",numbered=True)
        bill+=adds[added]
    # But what if the person wants mayo AND lettuce?***
    quantity=pyp.inputInt("How many sandwiches do you wanna order?\n",min=1)     
    return(quantity*bill)
    #But what if the customer wants another sandwich with different customisations?

final_bill=order()  
print(f"Your total bill is: Rs.{final_bill}. Happy meal!")


# ***checkout tkinter and curses