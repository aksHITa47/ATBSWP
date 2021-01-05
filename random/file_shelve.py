from pathlib import Path
import os
import shelve
print(Path.cwd())
#shelfFile = shelve.open('len.py')
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(type(shelfFile))
print(shelfFile['cats'])
#print(list(shelfFile.items()))
shelfFile.close()
app=open(Path.cwd()/'practice_ques'/'chap_8.txt','a')
app.write('Appended using the open() method \n')
app.close()
app2=open(Path.cwd()/'practice_ques'/'chap_8.txt','a')
app2.write('2nd appendement \n')
app2.close()
# Appends both files 'chap_8.txt', unless ofc specified ..practice_ques.