# def countdown(num):
#     for i in range(num, -1, -1):
#         print(i)
#         # countdown(num-1)


# countdown(14)

###############################


# def printReturn(a,b):
#     print(a)
#     return(b)

# print(printReturn(3,2))

##############################

# def first_plus_length(arr):
#     return arr[0] + len(arr)

# print(first_plus_length([1,2,3,4,5,6,7]))

#######################

def values_greater_than_second(arr):
    i = 0
    amount = 0
    newArr = []
    if(len(arr) < 2):
        return False
    else:
        while(i <= len(arr) - 1):
            if(arr[i] > arr[1]):
                amount += 1
                newArr.append(arr[i])
                i += 1
            else:
                i += 1
    print(amount)
    return newArr

print(values_greater_than_second([1,2,3,4,5,6,78,8]))
print(values_greater_than_second([1]))

#########################

# def length_and_value(a,b):
#     arr = []
#     while(len(arr) < a):
#         arr.append(b)
#     return (arr)

# print(length_and_value(10,33))