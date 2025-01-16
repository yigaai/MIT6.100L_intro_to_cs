MIT6.100L Lecture04 LOOPS OVER STRINGS, GUESS-AND-CHECK, BINARY 

break STATEMENT 
    a. immediately exits whatever loop it is in 
    b. skips remaining expressions in code block --> exits only innermost loop 

while <condition_1>: 
  while <condition_2>:     --> evaluated when <condition_1> and <condition_2> are True 
    <expression_a>    
    break                  --> will exit loop surrounds break 
    <expression_b>         --> never be evaluated (do not write code like this) 
  <expression_c>           --> evaluated when <condition_1> is True 



STRINGS & LOOPS
# BIG IDEA: The sequence of values in a for loop isn't limited to numbers. 
s = 'demo loops - fruit loops'
for char in s:
    if char in 'iu':
        print(char)
print("There is an 'i' or 'u'.")


# PRACTIE
s = 'abca'
seen = ''
n = 0
for char in s:
    if char not in seen:
        seen = seen + char
        n += 1
print(seen)
print(n) or print(len(seen))
# IDEA: write logic on paper before coding 



# GUESS-AND-CHECK
    a. a process called exhaustive enumeration 
    b. Applied to problem where:  
        --> be able to guess a value for solution 
        --> be able to check if the solution is correct 


# GUESS-AND-CHECK: SQUARE ROOT

guess = 0
x = int(input('enter an integer:'))
while guess**2 < x:
    guess += 1         --> exit loop when guess**2 >= x 
if guess**2 == x:
    print(f'The square root of x is {guess}.')
else:
    print('x is not a perfect square.')


# What if x is negative? --> while loop immediately terminates 
# --> So, could check for negative input,and handle differently 

guess = 0
neg_flag = False
x = int(input('enter an integer:'))
if x < 0:
    neg_flag = True    --> Boolean is used as a signal that negative x happens 
while guess**2 < x:
    guess += 1         --> exit loop when guess**2 >= x 
if guess**2 == x:
    print(f'The square root of x is {guess}.')
else:
    print('x is not a perfect square.')

if neg_flag:            --> condition has been True 
    print(f'Just checking... did you mean, {-x}, ?')


# PRACTICE 
# Write a program that checks through all the numbers from 1 to 10,
# prints the secret number if it's in that range,
# If it's not found, it doesn't print anything. 
secret_number = 4
for i in range(1, 11):
    if i == secret_number:
       print(f'Yes, it is secret number {i}.')

# If it's not found, prints that it did not find. 
secret_number = 56
found = False
for i in range(1, 11):
    if i == secret_number:
        print(f'Yes, it is secret number {i}.')
        found = True    --> something has happened 
if not found:           --> in order to print once --> exit the loop 
    print('It did not find.')

# BIG IDEA: Boolean can be used as signals that something happened. We call them Boolean Flags.  
  
  
# GUESS-AND-CHECK CUBE ROOT: POSITIVE & NEGATIVE CUBES 
cube = int(input('enter a integer:'))

for guess in range(abs(cube) + 1):
    if guess**3 == abs(cube):            --> step1. assume cube is positive 
        if cube < 0:                     --> step2. Deal with negative cuhe here 
            guess = -guess
        print(f"Cube root of {cube} is {guess}.")


# GUESS-AND-CHECK CUBE ROOT:JUST A LITTLE FASTER
cube = int(input('enter an integer:'))

for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break                                --> Terminate search once you know it have passed possible answer 
if guess**3 != abs(cube):                    --> Check why you exited the loop(i.e., greater or equal?) and decide if the guess is not a perfec loop 
    print(f'{cube} is not a perfect cube.')
else:
    if cube < 0:
        guess = -guess
    print(f'Cube root of {cube} is {guess}.')


# GUESS-AND-CHECK WITH WORD PROBLEMS 
for Alyssa in range(11):
    for Ben in range(11):                                 --> for each value of alyssa, check all possible values
        for Cindy in range(11):                           --> for each pair of alyssa and ben, check all possible values 
            total = (Alyssa+Ben+Cindy == 10)              --> 3 Booleans for word problems equations 
            two_less = (Ben == Alyssa - 2)
            twice = (Cindy == 2*Alyssa)
            if total and two_less and twice:              --> solutions found when all 3 hold  
                print(f'Alyssa sold {Alyssa} tickets.')
                print(f'Ben sold {Ben} tickets.')
                print(f'Cindy sold {Cindy} tickets')

                 
# MORE EFFICIENT WITH BIGGER NUMBERS
for Alyssa in range(101):
    Ben = max(Alyssa-20, 0)
    Cindy = Alyssa * 2
    if Alyssa + Ben + Cindy == 100:
        print(f'Alyssa sold {Alyssa} tickets.')
        print(f'Ben sold {Ben} tickets.')
        print(f'Cindy sold {Cindy} tickets')



















