import pyinputplus as pyp # as can be followed by whatever name we wanna use it.
while True:
    response=pyp.inputYesNo("Wanna keep an idiot busy?\n", allowRegexes=[r'y',r'n'])
    if response=='no' or response=='n':
        print("Bazinga!") 
        break
res=pyp.inputInt()
a=pyp.inputFloat()
print(res)
print(a)