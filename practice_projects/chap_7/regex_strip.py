import re
def rest(string,char):
    stripRegex=re.compile(r'\S{1,}(.*)\S')
    mo=stripRegex.search(string)
    if char=='':                                                                      
        return(mo.group())                                                                  
    else:
        strip=re.compile(r'%s'%char)
        return(strip.sub('',string))
        #c=mo.group() 
        #return(c.replace(char,''))     # This also works just fine but re.sub() is more "regex-y" xD

ent=input("Enter the string: ")
sep=input("Enter the character to be stripped (or press enter if no character is to be stripped): ")
print(rest(ent,sep))

# Also, need to figure out how to use re.sub() for char!=''


#THE FIRST TRY: 
# Too bulky!
 #if char=='':                                                                                                                                     
        #stripRegex=re.compile(r'\S{1,}(.*)\S')
        #mo=stripRegex.search(string)
        #print(mo.group())
        #print(len(mo.group())) #To check if trailing spaces were getting removed
 #else:
        #stripRegex=re.compile(r'\S{1,}(.*)\S')    
        #mo=stripRegex.search(string)
        #c=mo.group()
        #print(c.replace(char,''))
        #print(len(mo))
        #print(mo.group())

# With the function call:
 # if sep!='':
 #    rest(ent,sep)
 # else:
 #    rest(ent,'')
   

# ALSO, how to use 'char' variable in regex character class T_T, re.compile(r'[^char]') is not working :( ***



# UPDATE on ***
# mo=re.compile(r'%s'%char) or
# mo=re.compile(r'[^{}]'.format(char))