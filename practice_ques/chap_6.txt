1. What are escape characters?
   
   Escape characters represent characters in string values that would otherwise be difficult or impossible to type into code.
   They begin with '\'


2. What do the \n and \t escape characters represent?
   
   newline and tab respectively


3. How can you put a \ backslash character in a string?
   
   \\


4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
   
   Because we have used double quotes to represent the string.


5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
   
   With multiline strings using 3 single or double quotes.


6. What do the following expressions evaluate to?

    'Hello, world!'[1]                'e'
    'Hello, world!'[0:5]             'Hello'
    'Hello, world!'[:5]              'Hello'
    'Hello, world!'[3:]              'lo, world!'


7. What do the following expressions evaluate to?

    'Hello'.upper()                     'HELLO'
    'Hello'.upper().isupper()            True
    'Hello'.upper().lower()             'hello'


8. What do the following expressions evaluate to?

    'Remember, remember, the fifth of November.'.split()
    '-'.join('There can be only one.'.split())

    ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
    'There-can-be-only-one.'


9. What string methods can you use to right-justify, left-justify, and center a string?
   
   rjust(),ljust(),center()


10. How can you trim whitespace characters from the beginning or end of a string?
    
    lstrip() and rstrip()