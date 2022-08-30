#function WHY?
# Return Something
#Can be Called
#SAVE SPAVE

from sys import base_prefix

def function_name(paramet_one, parameter_two):
    pass

a = 59
b = 65
c = a + b
print(c)

a = 90
b = 80
c = a + b
print(c)


def determine_speed(miles, hours):
    print(f"Calculating speed when we travel {miles} in {hours}")
    # print(miles/hours) #print only logs to terminal
    return miles/hours

print(determine_speed(300,2))


# def range(start, step = 1, stop =0):