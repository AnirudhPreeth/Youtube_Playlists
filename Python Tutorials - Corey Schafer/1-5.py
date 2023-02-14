#Python Tutorials - Corey Schafer. 
#https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

#This is the notes for the entire playlist and code as well. 

#This file contains the notes and the code for videos 1-5. 

'''
Python is pre-installed in Mac. 
python--version
IDLE. python3 --version
nano ~/.bash_profile
Path variable allows Python 3 commands to work. 
alias python=python3 

Windows. 
cmd - Command Prompt.
python --version
IDLE. 

python - Opens Interactive Prompt. 
exit()
IDLE - Interactive prompt. (>>>) Full-fledged file editor.

Comments are usually ignored. They don't run on compiler. 
Editors - Sublime text, Atom.
IDE - Pycharm. 
'''
print("Hello World.")
x = 10
print(x)
#This is a single inline comment. 

'''
Python operates on Whitespace alone. Very clean language. 
Variables are usually all lowercase and if it is multiple words we separate those with underscore. 
Single quotes and double quotes are fine for string. 
len function - length. 
Index and it starts with 0. 
Slicing. 
Functions and methods are basically the same thing. 
Method is just a function that belongs to an object. 
Return statements.
Formatted string.
f-strings.
'''
message = "Hello World"
print(message)
my_message = "Hello World"
print(my_message)
print('Hello World')     #single quote.
print("Bobby's World")   #Both quotes. 
print('Bobby\'s World')  #Backslash to avoid error. 
message = """Bobby's World was a good cartoon in the 1990's"""
print(message)

message = "Hello World" 
print(len(message))
print(message[0])
print(message[10])
print(message[0:5]) #Range. First index is inclusive, second index is not. 
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))  #6th Index.
print(message.find('Universe'))

message = "Hello World" 
new_message = message.replace('World', 'Universe')
print(new_message)

message = "Hello World" 
message = message.replace('World', 'Universe')
print(message)

greeting = "Hello"
name = "Michael"
message = greeting + ', ' + name + ". Welcome!"
print(message)

greeting = "Hello"
name = "Michael"
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)
#Placeholders. 

greeting = "Hello"
name = "Michael"
message = 'f{greeting}, {name}. Welcome!'
print(message)

greeting = "Hello"
name = "Michael"
message = 'f{greeting}, {name.upper()}. Welcome!'
print(message)

greeting = "Hello"
name = "Michael"
print(dir(name)) #Attributes and methods. 

print(help(str))  #Help needs to run on string class. 
print(help(str.lower()))

'''
type() function

Arithmetic Operators - 
Addition            3+2
Subtraction         3-2
Multiplication      3*2
Division            3/2
Floor Division      3//2
Exponent            3**2
Modulus             3%2

Comparisons -
Equal               3==2
Not Equal           3!=2
Greater Than        3>2
Less Than           3<2
Greater or Equal    3>=2
Less or Equal       3<=2

Mod 2 on any number -> 0 is even, 1 is odd.
Boolean. 
'''
num = 3
print(type(num))

num = 3.14
print(type(num))

print(3/2)
print(3//2)
print(3**2)
print(3%2)
print(3*2+1)
print(3*(2+1))

num = 1
num = num + 1 #increment.
print(num)

num = 1
num+=1 
print(num)

num =1
num *=10
print(num)

print(abs(-3))
print(round(3.75))
print(round(3.75, 1))

num_1 = 3
num_2 = 2
print(num_1 == num_2) #False. Conditional Statements. 
print(num_1 != num_2) #True.
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

num_1 = '100'
num_2 = '200'
print(num_1 + num_2) #100200. As these are strings.

num_1 = '100'
num_2 = '200'
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2) #Casting. 

'''
Tuples allow us to work with sequential data and Sets are unordered collection of values with no duplicates. 
List - allows us to work with a list of values.  
Insert takes two argument. First the index to insert the value, value itself. 
Extend method. Only if multiple values are to be added to the list.
Pop returns the value that it removes. 
Sorted function doesn't sort the list in place. It returns a sorted version of the list. 
Tuples are the same as list just that tuples cannot be changed ever.
This is called mutable and immutable. 
Lists are mutable and tuples are not. They are immutable. 
'''
courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2]) #Go to but not including.
print(courses[:2])
print(courses[2:]) #slicing.

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.append('Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop() #Removes last item.
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort() #Alphabetical order(string)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
courses.sort() 
nums.sort()
print(courses)
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]
courses.sort(reverse=True)  #Descending order. 
nums.sort(reverse=True)
print(courses)
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted(courses) 
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses =sorted(courses) 
print(sorted_courses)

nums = [1, 5, 2, 4, 3]
print(min(nums)) #Minimum number

nums = [1, 5, 2, 4, 3]
print(max(nums))

nums = [1, 5, 2, 4, 3]
print(sum(nums))

courses = ['History', 'Math', 'Physics', 'CompSci']
print(courses.index('CompSci'))

courses = ['History', 'Math', 'Physics', 'CompSci']
print('Art' in courses)  #in operator. 
print('Math' in courses)

courses = ['History', 'Math', 'Physics', 'CompSci']           
for item in courses:
    print(item)    #access each value as we are looping through

courses = ['History', 'Math', 'Physics', 'CompSci']
for course in enumerate(courses):
    print(course)

courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses):
    print(index, course)

courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses, start=1):
    print(index, course)

courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ', '.join(courses)
print(course_str)

courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ' - '.join(courses)
print(course_str)

courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ', '.join(courses)
new_list = course_str.split(' - ')
print(course_str)
print(new_list)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1)
print(list_2)

#tuple example. 
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art' - This is an error as this is immutable. Tuples cannot be changed.


