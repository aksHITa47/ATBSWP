from pathlib import Path
import os
print(Path.cwd())
# /home/akki/atbswp
#os.chdir('/home/akki/bored')
#print(Path.cwd())
# /home/akki/bored
print(Path.home())
#os.makedirs('/home/akki/atbswp/practice_ques/chap_9.txt')
#Path('/home/akki/atbswp/practice_ques/chap_10.txt').mkdir() # mkdir() makes only a single directory at a time unlike os.makedirs(), that can make directories and sub-directories, both of 'em create folders, not files!

print(os.path.abspath('.')) # prints /home/akki/atbswp and not /home/akki/atbswp/random/path.py ??
print(os.path.abspath('./chap_8.txt')) # works only for the first directory inside the homedir, here it's atbswp, and not the sub-directory practice_ques where chap_8.txt really is
print(os.path.abspath('./chap_7.txt'))
print(os.path.abspath('./practice_ques/chap_8.txt')) 
print(os.listdir(Path.cwd()))
print(os.listdir(Path.home()))

p=Path('/home/akki/atbswp/')
q=Path('/home/akki/atbswp/practice_ques')
print(list(p.glob('*')))
print(list(p.glob('*.txt')))
print(list(q.glob('chap_?.txt')))