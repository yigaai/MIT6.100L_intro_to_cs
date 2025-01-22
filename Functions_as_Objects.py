MIT6.100L LEC08 FUNCTIONS as OBJECTS 


# WHAT IF THERE IS NO RETURN KEYWORD 
  a. python returns the value None --> represents the abscence of a value 
  b. No static semantic error generated 



# RETURN vs. PRINT 
return:
  a. only has meaning inside a function 
  b. only one return executed inside a function 
  c. code inside function not exexuted after return statement 
  d. has a value associated with it, given to function caller  

print:
  a. can be used outside the function 
  b. can execute many print statements inside a function 
  c. code inside a function can be executed after a print statement 
  d. has a value associated with it , outputted to the console 
  e. print expression itself returns None value 
      e.g., print(print(2+3)) --> None 



# PRACTICE 
def is_triangular(n):
    """
    :param n: n is an int > 0
    :return: returns True if n is triangular,
    i.e. equals a continued summation of natural numbers (1+2+3+...+k),
    False otherwise
    """
    total = 0
    for i in range(n):
        total += i
        if total == n:
            return True
    return False 



# FUNCTIONS SUPPORT MODULARITY 

HERE is bisection square root method as a function:  


def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    midpoint = (low + high) / 2.0

    while abs(midpoint**2 - x) >= epsilon:
        if midpoint**2 > x:
            high = midpoint
        else:
            low = midpoint
        midpoint = (low + high) / 2.0

    return midpoint


# write a function that satisfies the following specs

def count_nums_with_sqrt_close_to(n, epsilon):
    """
    :param n:         is an int > 2
    :param epsilon:   a positive number < 1
    :return:          returns how many integers have a square root within epsilon of n
    """
    count = 0
    for i in range(n**3):
        sqrt = bisection_root(i)
        if abs(sqrt-n) <= epsilon:
            print(f'sqrt of {i} is {sqrt}')
            count += 1
    return count


print(count_nums_with_sqrt_close_to(10, 0.1))



#FUNCTION SCOPE 

# UNDERSTANDING FUNCTION CALLS 
IT CREATES A NEW ENVIRONMENT WITH EVERY FUNCTION CALL
  a. like a mini program that it needs to complete 
  b. the mini program runs with assigning its parameters to some inputs 
  c. it does the work (aka the body of the function)
  d. it returns a value 
  e. the environment disappears after it returns the value (so the var which the enviro creates will also disappeares)



# SCOPE 
  a. Inside a function, can access/grab a var defined outside 
  b. Inside a function, cannot modify a var defined outsie 
  c. use Python Tutor to step through
  


# FUNCTIONS as ARGUMENTS 
# HIGHER ORDER PROCEDURES 

  a. Objects in Python have a type
      int, float, Boolean, NoneType, function

  b.Objects (functions are also first class objects)
      --> (functions) can be used as an argument to a procedure (another function)
      --> (functions) can be returned as a value from a procedure (by aother function)  

  # BIG IDEA: Everything in Python is an object. 



# PRACTICE 
def apply(criteria, n):
    """
    :param criteria: criteria is a func that takes in a number and returns a bool
    :param n:        n is an int
    :return:         returns how many ints from 0 to n (inclusive) math the criteria
    """
    count = 0
    for i in range(n + 1):
        if criteria(i):
            # in order to return a bool --> add if   
            count += 1
    return count


def is_even(x):
    return x % 2 == 0

def is_four(x):
    return x == 4 


print(apply(is_even, 10))
print(apply(is_four, 10)) 














