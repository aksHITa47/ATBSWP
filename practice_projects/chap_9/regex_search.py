import re
from pathlib import Path
reuse=input("Enter the regex to be searched:\n")
path=Path.cwd()/'dump'
find_regex=re.compile(r'%s'%(reuse))
for file in list(path.glob('*.txt')): # list()!
    print(file)
    readfile=open(file)
    data=readfile.read()
    match=find_regex.findall(data)
    print(match)


