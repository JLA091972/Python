
#1 - Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1 -- Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0]=15
print(x)

#1.2 -- Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = 'Bryant'
print (students[0])

#1.3 -- In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])

# #1.4 -- Change the value 20 in z to 30
z[0]["y"]=30
print(z[0]["y"])


##2 - Iterate Through a List of Dictionaries
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(studentslist):
    for each_key in range(len(studentslist)):
        # print(studentslist[each_key])
        for key, val in studentslist[each_key].items():
            print(key,'-',val)
    
iterateDictionary(students)


##3 - Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)



# #4 - Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo (somelist):
    for key in somelist:
        print(len(somelist[key]),key)
        for each in somelist[key]:
            print(each)

printInfo (dojo)