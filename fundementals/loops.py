# Loops

# for loops
# for ____ in ____:
#     pass

# first blank is the iterative variable <--- represents each single from the sequence thing that iterates over
# ex/ [1,2,3,4,5] iterative variable will represent each number in turn
# second blank is the sequance in iterate over
# ex/ range

# for i in range(5):
#     print(i)
#range(start, stop, step)
# start is inclusive and defaults to 0
# stop is exclusive (will stop before this number)
# step is the increment

# fruits = ['mango', 'banana', 'tomato', 'pear', 'apple']

# for fruits in fruits:
#     print(fruits)

for i in range(50, -1, -1):
    print(i)
    if i == 10:
        continue
    if i == 8:
        break


# FOR IN DICTS

# dog = {
#     'name': 'spot',
#     'age': 3,
#     'color': 'brown',
# }

# # for prop in dog:
# #     print(prop)
# #when we loop over a dictionary, the interative variable will be the key

# for key in dog:
#     print(f"{key}: {dog[key]}")


# # LIST of DICTS
# dog_list = [
#     {
#     'name': 'spot',
#     'age': 3,
#     'color': 'brown',
#     }
#     {
#     'name': 'fido',
#     'age': 6,
#     'color': 'black',
#     }
# ]


# # for dog in dog_list:
# #     print(dog)

# for dog in dog_list:
#     print(f'{dog['name']} will print now)
#     for key in dog:
#             print(f"{key}: {dog[key]}")



# # while loops (ctrl + c, ends the code)

# i = 0
# while(i<10):
#     print(i)

