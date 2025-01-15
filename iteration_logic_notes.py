# MIT6.100L LEC03 ITERATION 


# BRANCHING
if <exit right>:
    <set background to woods> 
    if <exit right>:
        <set background to woods>
        if <exit right>:
            <set background to woods>
            and so on and on and on... 
        else:
            <set background to exist>
    else:
        <set background to exit>
else:
    <set background to exit>


--> transform to while loops:


  
# while LOOPS
while <exist_right>:
  <set background to woods>
  <ask user which way to go> 
<set background to exit>



# CONTROL FLOW: while LOOPS 
while <condition>:     --> evaluates to a Boolean 
  <code>               --> if condition is True, execute all the steps inside the while code block
  <code>
   ...                 --> check <condition> again, 
                       --> repeat until <condition> is False 
                       --> if <condition> is never False, then will loop forever 



# while LOOP EXAMPLE 
# EXAMPLE 1 
where = input('You are in the Lost Forest. Go left or right?')
while where == 'right':
    where = input('You are in the Lost Forest. Go left or right?')
print('You got out of the Lost Forest!')


# Expand this code to show a sad face when the user entered the while loop more than two times
where = input('You are in the Lost Forest. Go left or right?')
times_of_right = 0
while where == 'right':
    times_of_right += 1
    if times_of_right > 2:
        print(':(')
    where = input('You are in the Lost Forest. Go left or right?')
print('You got out of the Lost Forest!') 


# EXAMPLE 3 
n = int(input('enter a non-negative integer:'))
while n > 0:
    print('x')
    n -= 1   --> inside the while loop 
  
# BIG IDEA: while loops can repeat code inside indefintely, sometimes need our intervention to end the code


# Iterate through numbers in a sequence 
n = 0          --> set loop variable outsiede while loop 
while n < 5:   --> test loop variable in condition 
  print(n)
  n = n+1      --> increment loop variable inside while loop 
  


# for LOOPS 
# CONTROL FLOW: while LOOPS vs. for LOOPS 
# verbose with while loop:
n = 0          
while n < 5:   
  print(n)
  n = n+1 
# shortcut with for loop: 
for n in range(5):
  print(n)


# STRUCTURE of for LOOPS
for <variable> in <sequence of values>: 
    <code>     --> first time, <variable> is the first value in sequence 
    <code>     --> next time, <variable> gets the second value in sequence 
    ...        --> until <variable> runs out of values


# RANGE
  a. Generates a sequence of ints, following a pattern 
  b. range(start, stop, step) 
  c. often omit start and step 
      e.g., for i in range(4) 
      e.g., for i in range(3, 5) 
  d. a lot like slicing in strings 
        --> string slicing: using colons and square brackets 
        --> range: using commas and parantheses


# RUNNING SUM 
mysum: a variable to store the running sum 
mysum = 0 
for i in range(10):
  mysum += i 
print(mysum)

# PRACTICE FOR RUNNING SUM 
# Get the total sum between and including those values 
# for example, if start = 3 and end = 5 then the sum should be 12. 
total_sum = 0
start = 3
end = 5
for i in range(start, end+1):
  total_sum += i
print(total_sum)

# BIG IDEA: 
  a. for loops only repeat for however long the sequence is 
  b. the loop variables takes on these values in order 

# SUMMARY 
    a.Looping mechanisms: while and for loops 
    b. while loops
          --> loop as long as a condition is True 
    c. for loops
          --> can loop over ranges of numbers 
          --> can loop over elements of a string 
            










