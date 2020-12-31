#import copy

def addToInventory(inventory, addedItems):
    #work=copy.copy(inventory) # Runtime Error otherwise: Length of dictionary changes during iteration
    # No need for copy(). Instead of first going through the inventory & then the addedItems, go through the addedItems and check if the key already exists 
    # in the inventory or not ***
    for i in addedItems:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory.setdefault(i,1)
    return(inventory)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+ ' '+ k)
        item_total+=v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby','dagger']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

# Clear doubt
# ***

# NOTE: RIGHT DOWN THE DOUBT SO AS TO NOT FORGET WHAT THAT WAS IN THE FIRST PLACE!! T_T