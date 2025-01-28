MIT6.100L LEC09 LAMBDA FUNCTION, TUPLES AND LISTS 

# FROM LAST LECTURE 
def apply(criteria, n):
    """
    :param criteria:  function that takes in a number and returns a bool
    :param n: an int
    :return: returns how many ints from 0 to n (inclusive) match the criteria
    """
    counts = 0
    for i in range(n+1):
        if criteria(i):
          # step1; takes in a number 
          # step2: use if to return a bool 
            counts += 1
    return counts


def is_even(x):
    return x % 2 == 0


print(apply(is_even, 10))



# ANONYMOUS FUNCTIONS (LAMBDA FUNCTIONS) 
  a. sometimes don't want to name functions, especially simple ones. 
      def is_even(x):
        return x % 2 == 0

  b. use an anonymous procedure by using lambda (no return keyword) 
      lambda x: x % 2 == 0 

  c. lambda function is one-time use (because it has no name) 



# COMPOUND DATA TYPES 
a. review: 
    -->scalar types: int, folat, bool 
    --> one compound type: string  

b. more general compound data types:
    indexed sequences of elements, which could themselves be compound structures 
    --> tuples: immutable 
    --> lists:  mutable 



# TUPLES 
a. indexable ordered sequence of objects 
b. objects can be any type: int, string, tuple, tuple of tuples... 
c. immutable: cannot change element values 

te = ()                 --> empty tuple 
ts = (2,)               --> tuple with one element --> compare to ts = (2) (type is int)

t = (2, "mit", 3)       --> multiple elements in tuples separated by commas  
t[0]                    --> evaluates to 2 
t + (5, 6)              --> a new tuple (2, 'mit', 3, 5, 6)
t[1:2]                  --> slice tuple --> ("mit", ) 
t[1:3]                  --> ("mit", 3) 
len(t)                  --> 3 
max(3, 5, 0)            --> 5 
t[1] = 4                --> gives error, can't modify object 


d.  an element of a squence is at an index which starts at 0  
    --> interating over sequences 
    for e in t:
      print(e)



# WHY TUPLES? 
    a. conveniently used to swap variable values 

      1. initial code: 
          x = 1
          y = 2

          temp = x
          x = y
          y = temp

      2. use tuple:
          x = 1 
          y = 2 
          (x, y) = (y, x) 

      b. used to return more than one value from a function 

          def quotient_and_remainder(x, y):
            q = x // y 
            r = x % y 
            return q, r  
            # one object with two elements 

          (quot, rem) = quotient_and_remainder(5, 2)
          print(quot, rem)
          # prints quot and rem as separate values, with a space in between.
          print((quot, rem))
          # will print the tuple (2, 1) 


# BID IDEA:Returning one object(a tuple) allows you to return multiple values (elements of tuple) 



# PRACTICE 
def char_counts(s):
    """
    :param s: s is a string of lowercase chars
    :return: returns a tuple
            the first element is number of vowels
            the second element is the number of consonants is s
    """
    num_of_vowels = 0
    num_of_cons = 0
    for char in s:
        if char in 'aeiou':
            num_of_vowels += 1
        else:
            num_of_cons += 1
    return num_of_vowels, num_of_cons



# VARIABLE NUMBER OF ARGUMENTS 
a. python has some built-in functions that take variable number of arguments, e.g., min()
b. use *notation to have same capability 
    i.e., python takes the input and assign it to a tuple behind the scenes 

example: 
def mean(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)


mean_num = mean(1, 2, 3, 4, 5, 6)
print(mean_num)



# LISTS 
  a. indexable ordered sequence of objects 
  b. usually homogeneous (i.e., all integers, all strings, all lists) 
  c. but can contain mixed types (not common) 


# INDICES AND ORDERING (PART)
L = [2, 'a', 4, [1, 2]] 
len[L] = 4
[1, 2] + [3, 4] = [1, 2, 3, 4] 



# ITERATING OVER a LIST 
a. compute the sum pf elements of a list 
  # the first version 
  def sum_of_list(L):
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total


# more pythonic version 
# natural to capture iteration over a list inside a function 
def sum_of_list(L):
    total = 0
    for i in L:
        total += i
    return total


# add the length of elements of lists 
def len_sum(L):
    total = 0
    for e in L:
        total += len(e)
    return total



      

          














