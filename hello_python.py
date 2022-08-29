# # print("Hello World!")


# # x = "Hello Python"
# # print(x)
# # y = 42
# # print(y)


# ################

# #Variables

# x = 7
# name_of_variable = 'this is snake casing'
# #lower case with underscores, class names are capitalized
# GLOBAL_VAR = 'are all caps'

# ##################

# #Date Types


# #primitive
#     #Numbers
# num = 7
# num = 9.3

#     #strings
# string = "This is a string"
# string2 = 'This is also a string'
    
#     #boolean
#         #true or false value
# bool = True
# bool2 = False






# #composite

#     #lists (known as arrays in JS)
# list = [1,2,3,4,5,6]
# list2 = ['bob', 'kyle', 'susan']
# #         0       1         2       Zero indexed
# name = list2[1] #kyle

# # list[3] = 7 --------- changes index 3 to 7
# # print(list)

# #spread
# first_three = list[0:3]
# print(first_three)
# last_number = list[-1:]
# print(last_number)

# print(len(list)) #len() returns length

# print(max(list)) #max/min will return the highest/lowest value in the list, for strings looks alphabetically A-min, z-max

# list.sort(reverse=True) #reverses the list
# print(list)

# list2.pop() # removes last item
# print(list2)






#     #dictionaries (known as objects in JS)
# #{}
dog = {
    'name': 'spot',
    'age': 3,
    'color': 'brown',
}
# print(dog['name'])
# #{key: value}

# dog['name'] = 'Tiger' #changes name to Tiger
# print(dog)


# #checking if a key exists in a dictionary
# #1
# print(dog.get('favorite_food', 'not found'))
# #2
# if "favorite_food" in dog:
#     print('he has a fav')
# else: 
#     print('he does not')

# Removing values from dics
# del dog['name']
# print(dog)
#or
# namename = dog.pop('name')
# print(dog)
#or
# dog.clear() #clears everything!
# print(dog)


#     #tuples - IMMUTABLE LIST - Cannot be altered
# tuple = (1,2,3,4,5,6)
# tuple[3] = 7 #will produce an error












#conditionals

#if
#else
#elif - (else if)
# < > <= >= == != (not ==) or and

# if 'age' in dog:
#     print(f'Dog is {dog["age"]}')
# else:
#     print('Age unknown.')

if 'age' not in dog:
    print('dog does not have an age')
elif dog['age'] > 4:
    print('Dog is older than 4')
else:
    print('dog is less than 4')

# f = format, f'string{var}' assigns value