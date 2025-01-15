MIT6.100L Lecture1 Introduction 
# Programming is about writing receipes to generate facts. 
# key insight: programs are no different from other kinds of data. 


# an algorithm: 
   1) sequences of simple steps 
   2) Flow of control process that specifies when each step is executed 
   3) A means of determining when to stop 



# Aspects of Programming Language: 
  1) Primitive Constructs(programming): numbers, strings & simple operations 
  2) Syntax: 
            'hi'5 -->   not syntactically valid 
            'hi'*5 -->  syntactically valid 

  3) Static Semantics: 
            which syntactically valid strings have meaning (programs have only one meaning)
            'hi'+5 -->  syntatically valid but static semantic error 



  # python progrmas
  1) a program is a sequences of definitions and commands: defenitions evaluated, commands executed by python interpreter in a shell. 
  2) Commands: instruct interpreter to do something. 



  # OBJECTS
  1) progrmas manipulate data projects which have a type. 
  
  2) Scalar objects vs. Non-scalar Objects 
       a. scalar: cannot be subdivided
          --> int:  
                    represent intergers
                    e.g., 5, -100 
                    
          --> float:  
                    represent real numbers 
                    e.g., 3.27, 2.0 
                    
          --> bool:
                  represent Boolen values:
                  True and False  
                  
          --> NoneType: special and have one value --> None 
                  

       b. Non-scalar: have internal structure that can be accessed, but can not divide by a number  
          --> Sequences of chars:'abcd' 
          --> Lists 
          --> Dictionaries 


  # EXPRESSIONS
    a. combine objects and operators to form expressions 
    b. an expression has a value, which then has a type 
      --> Big Idea: replace complex expressions by one value 


# VARIABLES 
  a. cs variables is bounded to one single value at a given time 
  b. can be bounded to an expression (but expressions evaluate to one value!) 
  c. equal sign is an assignment --> bind a value to a variable name 





MIT6.100L Lecture2  Strings, Input/Output, and Braching 

# STRINGS
  a. Think of string as a sequence of case-sensitive characters
  b. Enclose in quotation marks or single quotes 
  c. Concatenate and reapeat strings: letters, special chars, spaces and digits
      b = "myself" 
      c = a + b 
      d = a + " " + b 
      silly = a * 3 


# STRING OPERATIONS 
  a. len() is a function: to retrieve the length of a string in the parentheses 


# GET ONE CHARACTER IN A STRING 
  a. square brackets used to perfom indexing 
    e.g., s = 'abc'
          index: s[0]  s[1]  s[2]      --> always starts at 0 
          index: s[-3] s[-2] s[-1]     --> last element is len(s)-1 or -1  


# GET A SUBSTRING 
    a.slice string using [start : stop : step] 
      --> get char at start ; up to and include stop-1 ; taking every step chars 
      --> if [start : stop] --> step = 1 by default 

# IMMUTABLE STRINGS 
  a. string are immutable  -- can not be modified 
  b. e.g., 
          s = 'car' 
          s[0] = 'b' --> gives an error 
                     --> You can create new objects that are versions of the original one
          s = 'b' + s[1:len(s)] --> s bound to a new object --> variable name can only be bounded to one object 
          

# INPUT/OUTPUT 
# PRITING 
  a. printing many objects in the same command:
    --> seperate objects using commans to output them separated by spaces 
    --> concatenate strings together using + to print as a single object
    --> e.g.: 
            a = "the"
            b = 3 
            c = "musketeers" 
            print(a, b, c) 
            print(a + str(3) + c) --> every piece being concateated must be a string 



# INPUT 
  a. input always returns a str --> must cast if working with numbers 
      e.g., num2 = int(input("Type a number: ")) 
            print(5*num2)  



# CONDITIONS FOR BRANCHING 
# TWO NOTIONS OF EQUAL 
  a. variable = value 
      --> change the stored value of variable to value, just an action 
  b. some_expression == another_expression  
      --> a test for equality 
      --> no binding is happening 
      --> expressions are replaced by values & computer does the comparison 
      --> replace the entire line with True or False 



# COMPARISON OPERATORS 
    a. Variables for comparison can be ints, float, strings, etc. 
    b. Comparisons below evaluate to the type Boolean: True and False 
    c. With strings, be careful about case-sensitivity: "March" != "march" 



# LOGICAL OPERATIONS ON BOOL 
    a and b are variable names (with Boolean values) :
    
    not a   --> True if a is False 
            --> False if a is True 

   a and b  --> True if both are True
            --> False if both are False 

  a or b    --> True if either or both are True  



# WHY BOOL? 
    a. When we get to flow of control, 
        i.e., braching to different expressions based on values 
              we need a way of knowing if condition is true 
        e.g., if something is true, do this, other wise do that(some other commands).  
      

      
# BRANCHING IN PYTHON 
if <condition>:  --> condition has a value of True or False 
    <code>       --> Indentation matters in python !! 
    <code>       --> Do code within if block if condition is True 
    ... 
elif <condition>: 
    <code> 
    <code>
    ... 
else:
    <code> 
    <code> 
    ... 
<rest of program>  



# BRANCHING EXAMPLE
# Let semantic structure matches visual structure! 
# Big Idea: Practice will help you build a mental model of how to trace the code 

work_time = int(input('work time:'))
sleep_time = int(input('sleeping time:'))

if (work_time + sleep_time) > 24:
    print('impossible!')
elif (work_time + sleep_time) >= 24:
    print('full plan!')
else:
    leftover = abs(24-work_time-sleep_time)
    print(f'{leftover} hours left of the day.')

print('end of the day')



# INDENTATION AND NESTED BRANCHING   

x = float(input('enter a number:'))
y = float(input('enter a number:'))

if x == y:
    print('x and y are equal.')
    if y != 0:
        print(f'therefore, x/y is {x/y}')
elif y < x:
    print('y is smaller')
else:
    print('x is smaller')

print('end the calculation')
      

      
# BIG IDEA 
a. Debug early, debug often. 
b. Do not write a complete program at once. It introduces too many errors.
c. Use the Python Tutor to step through code when you see something unexpected. 

          






          
          
  
  
  
      
