def collatz(number): # function definiton
# function code
    if number%2==0:
        print(number//2)
        return(number//2)
    elif number%2==1:
        print(3*number+1)
        return(3*number+1)
  
# main program
try:
    num=int(input("Enter number:"))
    # loop to keep calling the function
    while True:
        if num<=0:
            print("Please enter a non-zero positive integer")
            break
        else:
            rec=collatz(num)
            if rec!=1:
                num=rec
            elif rec==1:
                break
except ValueError: #input validation
    print("Error: Please enter an integer value")

    

   