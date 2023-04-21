num1 = 42 #variable declaration number
num2 = 2.3 #variable declaration float
boolean = True #variable declaration boolean
string = 'Hello World' #variable declaration string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuples
print(type(fruit)) #print to console, type check
print(pizza_toppings[1]) #print to console, list access value
pizza_toppings.append('Mushrooms') #print to console, add value
print(person['name']) #print to console, dictionary access value
person['name'] = 'George' #dictonary change value
person['eye_color'] = 'blue' #dictonary change value
print(fruit[2]) #tuples access value

if num1 > 45: # Conditional if, print to console 
    print("It's greater")
else: #Conditional else, print to console
    print("It's lower")

if len(string) < 5: # Conditional if - elif - else, print to console.
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop, 0 through 5
    print(x)
for x in range(2,5):#for loop, 2 through 5
    print(x)
for x in range(2,10,3):#for loop, 2 through 10, increments by 3
    print(x)
x = 0
while(x < 5): #while loop
    print(x)
    x += 1 #increments x

pizza_toppings.pop() #delete last value of a list
pizza_toppings.pop(1) #delete value at specified index

print(person) #print to console
person.pop('eye_color') #delete value of dictonary
print(person) #print to console

for topping in pizza_toppings: #for loop through a list
    if topping == 'Pepperoni': #conditional if
        continue
    print('After 1st if statement') #print string to console
    if topping == 'Olives': #conditional if
        break #stops loop

def print_hello_ten_times(): #function
    for num in range(10): #for loop
        print('Hello') #print to console

print_hello_ten_times() #call function

def print_hello_x_times(x): #function with parameter
    for num in range(x): #for loop
        print('Hello') #print to console

print_hello_x_times(4) #function call with arguement

def print_hello_x_or_ten_times(x = 10): #function with parameter
    for num in range(x): #for loop
        print('Hello')#print to console

print_hello_x_or_ten_times() #function call stops at 10
print_hello_x_or_ten_times(4) #function call stops at 4


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