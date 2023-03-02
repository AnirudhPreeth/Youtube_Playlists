#Python Tutorials - Corey Schafer. 
#https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

#This is the notes for the entire playlist and code as well. 

#This file contains the notes and the code for videos 6-10. 

'''
Video 6. 

Boolean. 
Object Identity : is
When we are using Object Identity we are actually checking if objects have the actual ID.
Or basically whether they are the same object in memory. 
Switch case statement - To check multiple values.
Python doesn't have a switch case statement. Because the if-elif-else statements do the job good enough already. 
Boolean Operations : AND, OR, NOT. 
Two objects can be equal but not the same object in memory. 

False Values : 
False 
None
Zero of any numeric type
Any empty sequence for example, '', (), [].
Any empty mapping, for example, {}.

To determine what Python evaluates to True or False, it's easier to show everything evaluated to False. 
And everything else, by default, evaluate to True. 
'''
if True:
    print("Conditional was true.")
    
if False:
    print("Conditional was true.") #Didn't print out anything. 

language = 'Python'
if language == 'Python':
    print("Conditional was true") 

language = 'Python'
if language == 'Python':
    print("Language is Python") 
else:
    print("No match")

language = 'Java'
if language == 'Python':
    print("Language is Python") 
else:
    print("No match")
    
language = 'Java'
if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java.") 
else:
    print("No match")

language = 'Java'
if language == 'Python':
    print("Language is Python")
elif language == 'Java':
    print("Language is Java.")
elif language == 'Javascript':
    print("Language is Javascript.") 
else:
    print("No match")

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print("Admin Page.")
else:
    print("Bad Creds.")

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print("Admin Page.")
else:
    print("Bad Creds.")
    
#If only one of these is true : OR keyword. 
user = 'Admin'
logged_in = False
if user == 'Admin' or logged_in:
    print("Admin Page.")
else:
    print("Bad Creds.")
    
#Not is used to switch a Boolean. 
user = 'Admin'
logged_in = False
if not logged_in:
    print("Please log in.")
else:
    print("Welcome.")

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  #True. 

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  #False. 
#These are two different objects in memory. 

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))
print(a is b)
#id's are different. 

a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a is b)
#True. They are the same. 

a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a == b)
#True.

a = [1, 2, 3]
b = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b)) #True. 

condition = False
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #Evaluates to False. 
    
condition = None
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #None evaluates to false as well. 

#If you have a numeric data type and you pass it into a condition, then zero will evaluate to False. 
condition = 0
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #False.
    
condition = 10
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #True. 

#If you have any empty (?) and pass it into a conditional, then that would evaluate to False.
#Empty string, empty list, empty tuple.  

condition = []
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #False.

condition = ''
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #False. 
    
condition = {}
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #False. 
    
#Let's say ypu have a function or something that is supposed to return some values, it's needed to check if those values are actually there. 
#Pass in these sequences into a conditional to check whether a string is empty or a dictionary is empty, and you don't have to call any ...
#...specific method. 
#You can just pass in the empty sequence or the empty dictionary and it will evaluate to True or False, if that is empty.
#There are some User defined Classes that will evaluate to False. 

condition = 'Test'
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #True. 


'''
Video 7. 

Two important keywords when working with loops -> break and continue. 
Break ->break out of a loop. 
Continue ->moves on to the next iteration of the loop. 
Loop within a loop. 
While loops will just keep going until a certain condition has been met or until we hit a break. 
'''
nums = [1,2,3,4,5]
for num in nums:
    print(num)

nums = [1,2,3,4,5]
for num in nums:
    if num ==3:
        print("Found!")
        break
    print(num)  #Printed only 1,2. The number did not get printed out. 
 
nums = [1,2,3,4,5]
for num in nums:
    if num ==3:
        print("Found!")
        continue
    print(num)  #Printed out 1,2 Found!, 4, 5. 
    
nums = [1,2,3,4,5]
for num in nums:
    for letter in 'abc':
        print(num, letter) #Every combinations. 

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i) #starts at 1 and goes up to but not 11. 

x = 0
while x <10:
    print(x)
    x +=1 #x from 0-9. 

x = 0
while x <10:
    if x == 5:
        break
    print(x)
    x +=1 #x from 0-4.

#To get infinite loop just replace comparison with True. 
x = True
while x <10:
    if x == 5:
        break
    print(x)
    x +=1 #Break to stop the loop. 

#If you get stuck in infinite loop press control+c to stop the loop. 

x = True
while x <10:
    print(x)
    x +=1 #Infinite Loop. 

'''
Video 8. 

Functions are basically some instructions packaged together to perform a specific task.  
def keyword -> definition.
It is possible to write a function and have no code in it, but we can't leave it completely blank.
To fill the function later, just type pass keyword.  
Pass keyword is saying we don't want to do anything with this for now, but it won't throw any errors for leaving it blank. 
We need to have the parenthesis when we run our function, in order to execute it. if we don't have those there, then it will be equal to...
...the function itself.    
Functions allow us to reuse our code without having to repeat ourselves. 
"Keeping your code dry" -> Don't repeat yourself. 
Return in function - Means that when we execute our function, its actually gonna be equal to our return value. 
Think of the function as a machine which takes input and produces a result. When you execute a function think of it as a black box.
You don't know how its doing what its doing, you're mainly concerned about the input and the return value. 

The format() method formats the specified value(s) and insert them inside the string's placeholder.
Your required positional arguments have to come before your key word arguments. If you try to give a function without those in order, its going to give an error.  
'''
def hello_func():
    pass

print(hello_func) #This is a function at a certain location in memory.
print(hello_func()) #None. As we are not doing anything with the function yet and we did not add a return value. 

def hello_func():
    print("Hello Function!")
hello_func() #Executed function.
#hello_func() as many times as we want. 

def hello_func():
    return 'Hello Function!' #No result. Just a string we're not doing anything with. 

def hello_func():
    return 'Hello Function!'
print(hello_func()) #Prints the statement.
print(hello_func().upper())

#Pass arguments in function - parameters.
def hello_func(greeting):
    return '{} Function!'.format(greeting)
print(hello_func('Hi')) #Hi function. 

#Python Scope. 

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi')) #Hi. As we passed in non value for name. 

def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)
print(hello_func('Hi', name = 'Corey')) #Hi, Corey

def student_info(*args, **kwargs):
    print(args)  #Allowing us to accept an arbitrary number of positional or keyword arguments.  
    print(kwargs) #Convention. 
student_info('Math', 'Art', name = 'John', age = 22)
#args - tuple with positional arguments. 
#kwargs - dictionary with all of our keyword values. 
#Function call with arguments using a * or **. When its used in that context, it will actually unpack a sequence or a dictionary and...
#...pass those values into the function individually.  

def student_info(*args, **kwargs):
    print(args)  
    print(kwargs)
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info('Math', 'Art', name = 'John', age = 22) 
student_info(*courses, **info)

#Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    '''Return true for leap years, false for non-leap years.'''
    return year%4 ==0 and (year%100 !=0 or year%400==0)
def days_in_month(year, month):
    '''Return number of days in that month in that year.'''
    if not 1<=month <=12:
        return 'Invalid month'
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]


  

