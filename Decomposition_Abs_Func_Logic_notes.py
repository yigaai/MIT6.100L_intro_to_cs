MIT6.100L LECTURE07 DECOMPOSITION, ABSTRACTION, FUNCTIONS 

# ABSTRACTION ENABLES DECOMPOSITION 
BIG IDEA: Apply abstraction (black box) and decomposition (split into self-contained parts) to programming. 


  
# SUPPRESS DETAILS with ABSTRACTION 
  In programming, think of piece of code as black box
      a. coder creates details: 
          --> hide tedious coding details 
          --> reuse black box at different parts in the code without copy & pasting 
      b. function works as a black box : produce an output from inputs,while hiding details of how it does the computation 



# FUNCTION 
  a. some code written in a special and resuable way
  b. capture steps of a computation so that we can use with any input 



# FUNCTION CHARACTERISTICS 
  a. name (think: variable bound to a function object ) 
  b. formal parameters (0 or more): the inputs 
  c. docstring (optional but recommended) 
      --> a comment delineated by triple quotes that provides a specification for the function  
  d. a body: a set of instructions to execute when function is called (function call)   
  e. Returns something  (Return is a key word) 


# HOW TO THINK ABOUT WRITING A FUNCTION 
  a. figure out the problem you have to solve  & what value you need to give back 
  b. Drawing pictures or writing processes on paper to  combine logic 

# e.g. want to know if i is even

def is_even(i):
    """
    :param i: a positive int
    :return: return True if it is even, otherwise False 
    """
    if i % 2 == 0:
        return True 
    else:
        return False 


--> since i % 2 == 0  is a Boolean that evaluates to True/False already 
--> make the code cleaner: 
def is_even(i):
    """
    :param i: a positive int
    :return: return True if it is even, otherwise False 
    """
    return i % 2 == 0

# BIG IDEA: At this point, all we've done is make a function object which stores in computer memory.  



# HOW TO CALL(INVOKE) A FUNCTION 
  a. name of the function: is_even 
  b. values for parameters: is_even(3) 
  c. is_even(3) replaced by the return 
      --> think about expression like 3+2, python replaced this expression by value 5 
      --> function is a kind of like expression -> return back one value --> that value will replace the function call 

# BIG IDEA: A function' code only runs when you call(aka invoke) the function 



# EXAMPLE: Suppose we want to add all the odd integers between (and including) a and b 
  a. figure out the problem: 
      --> input:  values for a and b 
      --> output: sum of odds between a and b  

  b. PAPER FIRST 
      --> start with a simple example on paper --> more complex example (systematically solve the problem) 
      --> combine logic on paper and then tell the logic to python through coding 

  c. CHOOSE BIG-PICTURE STRUCTURE 
      --> add ALL numbers between (and including) a and b: we need a loop 

  d. WRITE CODE 

    def sum_of_odds(a, b):
    sum_odds = 0
    for i in range(a, b+1):
        if i % 2 == 1:
            print(f'{i} is an odd number.')
            sum_odds += i
    return sum_odds 

# BIG IDEA: Solve a simpler problem first. Add functionality to the code later. 
# BIG IDEA: Test code often. Use prints to debug. 


# PRACTICE: 
def is_palindrome(s):
    """
    :param s: is a string
    :return: returns True if s is a palindrome and False otherwise
    """

    return s[:] == s[::-1]




 





















