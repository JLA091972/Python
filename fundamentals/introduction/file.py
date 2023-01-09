num1 = 42  # variable declaration initialize int
num2 = 2.3 # variable declaration initialize float
boolean = True #variable declaration initialize bool
string = 'Hello World' #variable declaration initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration initialize string array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration initialize string array
print(type(fruit)) #log statement
print(pizza_toppings[1]) #log statement
pizza_toppings.append('Mushrooms')  # Data Types string
print(person['name'])  #log statement
person['name'] = 'George' # variable declarationz
person['eye_color'] = 'blue' # variable declarationz
print(fruit[2]) #log statement

if num1 > 45:  # conditional if
    print("It's greater")  #log statement
else:  # conditional else
    print("It's lower")  #log statement

if len(string) < 5: # conditional if
    print("It's a short word!")  #log statement
elif len(string) > 15:  # conditional else if
    print("It's a long word!") #log statement
else: # conditional else
    print("Just right!")  #log statement

for x in range(5):  #for loop start
    print(x)  #for loop log statement
for x in range(2,5):  #for loop start
    print(x)  #for loop log statement
for x in range(2,10,3):  #for loop start
    print(x)  #for loop log statement
x = 0  # variable declaration
while(x < 5): #while loop start
    print(x)  #while loop log statement
    x += 1 #while loop increment value

pizza_toppings.pop()  # Data Types Composite delete value
pizza_toppings.pop(1)  # Data Types Composite delete value

print(person) #log statement
person.pop('eye_color') # Data Types Composite delete value
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #conditional if
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #conditional if
        break #for loop break

def print_hello_ten_times():  #Data Types function declaration
    for num in range(10):  #for loop start
        print('Hello')  #log statement

print_hello_ten_times()#Data Types function call

def print_hello_x_times(x):#Data Types function declaration
    for num in range(x):  #for loop start
        print('Hello')  #log statement

print_hello_x_times(4)#Data Types function call

def print_hello_x_or_ten_times(x = 10):#Data Types function declaration
    for num in range(x):  #for loop start
        print('Hello')  #log statement

print_hello_x_or_ten_times()#Data Types function call
print_hello_x_or_ten_times(4)#Data Types function call


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