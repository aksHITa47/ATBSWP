1. What are the two values of the Boolean data type? How do you write them? 

   The two boolean values are- true and false, written, True and False.

   
2. What are the three Boolean operators?

   The boolean operators are- *and*, *or* & *not*


3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

   1. True and True is True.
   2. True and False is False.
   3. False and True is False.
   4. False and False is False.
   5. True or True is True.
   6. True or False is True.
   7. False or True is True.
   8. False or False is False.
   9. not True is False.
   10. not False is True.


4. What do the following expressions evaluate to?

   1. (5 > 4) and (3 == 5)
      False

   2. not (5 > 4)
      False

   3. (5 > 4) or (3 == 5)
      True

   4. not ((5 > 4) or (3 == 5))
      False

   5. (True and True) and (True == False)
      False

   6. (not False) or (not True)
      True


5. What are the six comparison operators?
   
   ==, !=, <, >, <=, and >=.


6. What is the difference between the equal to operator and the assignment operator?
   
   '==' is the equal to operator that compares two values and evaluates to a Boolean, while '=' is the assignment operator that stores a value in a variable.


7. Explain what a condition is and where you would use one.
   
   Conditions are expressions that evaluate down to either *true* or *false*.


8. Identify the three blocks in this code:

spam = 0
if spam == 10:         #1(every statement inside this if statement)
    print('eggs')
    if spam > 5:
        print('bacon') #2
    else:
        print('ham')   #3
    print('spam')
print('spam')


9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
   
   if spam == 1:
    print('Hello')
   elif spam == 2:
    print('Howdy')
   else:
    print('Greetings!')


10. What keys can you press if your program is stuck in an infinite loop?
    
    ctrl+C


11. What is the difference between break and continue?

    The break statement skips the rest of the loop and jumps over to the statement following the loop. The continue statement forces the next iteration of the loop to take place, skipping any code in between.


12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
    
    They all do the same thing upon execution. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.


13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
    
   for i in range(1, 11):
      print(i)

   and:

   i = 0
   while i < 9:
      print(i)
      i = i + 1


14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
    
    The function call statement will be: spam.bacon()


    


