1. What does the code for an empty dictionary look like?
   
   {}


2. What does a dictionary value with a key 'foo' and a value 42 look like?
   
   {'foo':42}


3. What is the main difference between a dictionary and a list?
   
   The items in a dictionary are not ordered while in lists they are.


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
   
   KeyError error is raised


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
   
   No difference


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
   
   The first statement checks for the key 'cat' whereas the second statement checks whether there's any value 'cat' in any of the keys in spam


7. What is a shortcut for the following code?
if 'color' not in spam:
    spam['color'] = 'black'

    spam.setdeafult('color', 'black')


8. What module and function can be used to “pretty print” dictionary values?
   
   pprint.pprint() or print(pprint.pformat())