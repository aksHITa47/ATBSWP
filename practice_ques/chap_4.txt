1. What is []?
   
   An empty list.


2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
   
   spam[2]='hello'


For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
3. What does spam[int(int('3' * 2) // 11)] evaluate to?
   
   '3'*2='33', int('33')=33, 33//11=3, spam[3] is 'd'. So, it'll return 'd'


4. What does spam[-1] evaluate to?
   
   'd'


5. What does spam[:2] evaluate to?
   
   ['a','b'] as first index is taken as zero if nothing is specified


For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
6. What does bacon.index('cat') evaluate to?
   
   1


7. What does bacon.append(99) make the list value in bacon look like?
   
   [3.14, 'cat', 11, 'cat', True, 99]


8. What does bacon.remove('cat') make the list value in bacon look like?
   
   [3.14, 11, 'cat', True]. REmoves the first instance


9. What are the operators for list concatenation and list replication?
   
   '+' and '*;


10. What is the difference between the append() and insert() list methods?
    
    append() method adds the value at the end of the list whereas insert() allows us to specify the index where we want to insert the item in the list.


11. What are two ways to remove values from a list?
    
    del() method using the index and remove() using the value to be removed as argument


12. Name a few ways that list values are similar to string values.
    
    They can be concatenated and replicated, passed as an argument in len(), have indexes and slices and can be used for loops.


13. What is the difference between lists and tuples?
    
    Lists are mutable, meaning, they can have values added, removed, or changed. Tuples are immutable,i.e., they cannot be changed at all. Tuples are written using parentheses () while lists use the square brackets, []


14. How do you type the tuple value that has just the integer value 42 in it?
    
    a=(42,) 


15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
    
    a=list((42,34)) # List form of tuple
    b=tuple([1,2]) # Tuple form of list


16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
    
    The reference Id, to refer or point to the location in memory containing the list.


17. What is the difference between copy.copy() and copy.deepcopy()?
    
    copy.copy() is used when the variable refers to a list with non-list type values, whereas, copy.deepcopy() is used when the variable refers to a list containing list values.
