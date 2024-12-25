# # Write a nested function structure that uses both nonlocal and global variables to track different kinds of counts. For example, track total operations globally and successful operations locally.

# count = 0 # Variable
# def function():
#     innercount = 0 # Outer Variable
#     def trackinner():
#         nonlocal innercount # Outer Variable called Inside Function
#         innercount += 1
#         print(innercount)
#     def other():
#         global count # Global Variable called Inside Function
#         count += 1
#         print(count)

#     trackinner()
#     trackinner()
#     other()
#     other()

# if __name__ == '__main__':
#     function()

# # Create a function that accepts any number of positional and keyword arguments (*args and **kwargs) and prints them in a formatted way. Make it handle at least three different data types (strings, numbers, lists).

# def function(*args, **kwargs):
#     for i,arg in enumerate(args, start=1):
#         print(f"{i}: {arg}")
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# function(1,[5, 4], name= "adsf", age = 1)

# # Here's a debugging challenge:

# x = 0
# def outer():
#     x = 1
#     def inner():
#         # nonlocal x # OP : 2
#         # global x # OP : 1
#         x = x + 1  # This will cause an error
#         print(x)
#     inner()
# outer()

# # Can you explain why this code raises an error and fix it using either nonlocal or global? Error cuz the there is no x declared in inner()

# # Create a function that maintains a running average using a nonlocal variable. It should accept numbers one at a time and return the current average.

# count = 0
# currentAvg = 0
# def base():
#     runavg = 0
#     def runningAvg(distance):
#         nonlocal runavg
#         runavg += distance
#         global count ,currentAvg
#         count += 1
#         currentAvg = runavg / count
#         print(currentAvg)

#     runningAvg(15)
#     runningAvg(25)
#     runningAvg(35)

# if __name__ == '__main__':
#     base()