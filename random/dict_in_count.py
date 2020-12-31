dic={1:'w',2:'w'}
w=0
for i in dic.values(): 
    if i=='w':
        w+=1
    if w>1:
        print("invalid")
        break
print(w)
