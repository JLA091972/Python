#1 Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) 
# down to 0 (as the last element).

newlist=[]
def countdown(count):
    if (count >= 0):
        for x in range(count,-1,-1):
            # print(x)
            newlist.append(x)
    else:
        print(count)
    print(newlist)

countdown (5)


#2 Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.

def print_and_return(a):
    print(a[0])
    return(a[1])

print(print_and_return([1,2]))


#3 First Plus Length - Create a function that accepts a list 
# and returns the sum of the first value in the list plus the list's length.

def first_plus_length(a):
    lenght = len(a)
    # print("lenght :", lenght)
    # print("first value:", a[0])
    sum = a[0] + lenght
    return(sum)

print(first_plus_length([1,2,3,4,5]))


#4 Values Greater than Second - Write a function that accepts a list and creates a new list
# containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False
newlist = []
def values_greater_than_second(x):
    if (len(x) < 2):
        return(False)
    else:
        secondvalue = x[1]
        for i in range(0,len(x)):
            if x[i] > secondvalue:
                newlist.append(x[i])
    return(newlist)

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.


def length_and_value(x,y):
    newlist = []
    for i in range(0,x):
        newlist.append(y)
    return(newlist)

print(length_and_value(4,7))
print(length_and_value(6,2))


