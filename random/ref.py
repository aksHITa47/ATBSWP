def func(a):
    a=2
    print(id(a))

def lists(para):
    para.append(3)
    print(id(para))

c=4
arg=[1,2]
lists(arg)
print(id(arg))
print(arg)
func(c)
print(id(c))
print(c)

# In function call, values of the argument gets copied in parameter. For lists and dictionaries it is the REFERENCE ID that is used as parameter. 
# A new reference is created, but it points to the same object in memory, hence the same value returned by id()
# In list and dictionaries the argument and parameter variable POINT to the same 'Place' in memory, i.e., to the same object.

# In integer they are called by values instead of call by reference (remember Turbo C++)
