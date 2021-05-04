num1 = 42 # variable declaration, integer
num2 = 2.3 # variable declaration, float 
boolean = True # log statement
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] 
# list, list initialize, string
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# dictionary, dictionary initialize, string, bolean, integer
fruit = ('blueberry', 'strawberry', 'banana') # tuple, tuple initialize, string
print(type(fruit)) # log statement, single line, type check
print(pizza_toppings[1]) # log statement, access value [within list]
pizza_toppings.append('Mushrooms') # add value, string
print(person['name']) # log statement, string, access dictionary value
person['name'] = 'George' # change dictionary value
person['eye_color'] = 'blue' # list add value, add key value
print(fruit[2]) # log statement, access value

if num1 > 45: # conditional, condition if
    print("It's greater") # log statement, single line
else: #else condition
    print("It's lower")# log statement, single line

if len(string) < 5: # length check, conditional if, 
    print("It's a short word!") # log statement, single line
elif len(string) > 15: # length check, else if
    print("It's a long word!") # log statement, single line
else: # else condition
    print("Just right!") # log statement, single line
for x in range(5): # start for loop [for], iterator [x], (start at 0, increment by 1, break when x 10, stop loop)
    print(x) # log the output for the above 
for x in range(2,5): # for loop, start at 2, increment by 1 (default), and break when x = 5, stop loop
    print(x) # log the output for the above
for x in range(2,10,3):# for loop, start at 2 , increment by 3, break when x >= 10 (or 11 in this case), stop loop
    print(x) # log the ouput for the above
x = 0 # variable declaration, integer
while(x < 5): # while loop, "while" start, increment the x by 1 after logging statement (multi line), stop when x < 5
    print(x)# log given value of x 
    x += 1 # increment by 1

pizza_toppings.pop() # delete last key value in pizza_toppings string
pizza_toppings.pop(1) # delete the second position in the string sequence of pizza_toppings

print(person) # log statement, dictionary access value
person.pop('eye_color')# delete value in string sequence and it's key values within dicionary
print(person)# logs statement of line 43 with deleted 'eye-color' value

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # if condition, string
        continue # continue sequence for loop 
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if condition, string
        break #exit/stop loop

def print_hello_ten_times(): # function, function declaration
    for num in range(10): # parameter 10
        print('Hello') # argument 

print_hello_ten_times() # return, single line "Hello*10"

def print_hello_x_times(x): # function, function declaration 
    for num in range(x): # parameter, integer x
        print('Hello') # argument

print_hello_x_times(4) 
""" 
perform the function with the parameter of 4 (x) logging the argument Hello to get output "Hello*4"
"""
def print_hello_x_or_ten_times(x = 10): 
    """
    function, declaration function, variable declaration, integer, parameter
    """
    for num in range(x):  # variable, increment default 
        print('Hello') # argument 

print_hello_x_or_ten_times() # logs Hello*10
print_hello_x_or_ten_times(4) # error?


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)