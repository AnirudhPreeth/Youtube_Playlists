#Python Tutorials - Corey Schafer. 
#https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

#This is the notes for the entire playlist and code as well. 

#This file contains the notes and the code for videos 6-10. 

'''
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
#Pass in these sequences into a conditional to check whether a string is empty or a dictionary is empty, and you don't have to call any specific method. 
#You can just pass in the empty sequence or the empty dictionary and it will evaluate to True or False, if that is empty.
#There are some User defined Classes that will evaluate to False. 

condition = 'Test'
if condition:
    print("Evaluated to True.")
else:
    print("Evaluated to False.") #True. 


'''
Two important keywords when working with loops -> break and continue. 
Break ->break out of a loop. 
Continue ->moves on to the next iteration of the loop. 
Loop within a loop. 
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
        print(num, letter)
