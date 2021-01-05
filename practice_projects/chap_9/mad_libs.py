import re
from pathlib import Path
workp=Path.cwd()/Path('dump')
readfile=open(workp/Path('madlib.txt'),'r')
data=readfile.read()
readfile.close()
find=re.compile(r'(ADJECTIVE|VERB|NOUN|ADVERB)') #Finally
while find.search(data)!=None:
    rep=input("Enter an %s:\n"%(find.search(data).group().lower()))
    data=find.sub(rep,data,1) # fgs, don't forget the count argument for sub() or else the very first instance of a match will be substituted for all the matches.
writefile=open(workp/Path('madlib_a.txt'),'w')
writefile.write(data)
writefile.close()