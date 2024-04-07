
# True ,False ,None
# and,or,not,is
# if ,elif,else
# while,for,break ,continue,return,in,yield
# try,except,finally,raise,assert
# import,from,class,lambda,as,pass,global,nonlocale,del,with

import keyword
# print(keyword.kwlist)

print(len(keyword.kwlist))

# ['False', 'None', 'True', 
#  'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#    'finally', 'for', 'from', 'global', 'if', 'import', 
#  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

a=10
b=10
c=None
print(a==b)
print(a!=b)
print(c)

#use of None
def info(Name=None):
    if Name!=None:
        print('hello :',Name)
    else:
        print('name did\'t exist')

info('ram')
info()
#  other use is like when we don't want to send any value as retutn we can send None
# we can assign None for any object more ....................

# use of assert 


# The assert keyword in Python is primarily used for debugging and testing purposes. 
# It's used to test whether a condition is true, and if it's not, it raises an AssertionError exception. 
# Here are some common scenarios where you might use assert:

def division(x,y):
    assert y!=0
    print('not executing this line')
    return x/y
result=division(4,2)
result=division(12,1)
print(result)
# result=division(4,0)
print(result)

# Traceback (most recent call last):
#   File "reserve.py", line 52, in <module>
#     result=division(4,0)
#   File "reserve.py", line 46, in division
#     assert y!=0
# AssertionError

# Case:
#     Input Validation
#     Code Contracts:
#             def process_data(data):
#               # Process the data
#               assert isinstance(data, list), "Data should be a list"
# Debugging: During development, assert statements can be inserted into the code to 
# check whether certain conditions hold true. This can help quickly identify logical errors or unexpected behavior.

# python
# Copy code
# def calculate_discount(total):
#     assert total >= 0, "Total should be non-negative"
#     if total >= 100:
#         return total * 0.1
#     else:
#         return 0

# discount = calculate_discount(-10)  # Assertion error will be raised
# Testing: In unit tests and test-driven development (TDD), 
# assert statements are used extensively to verify the correctness of code. They provide a simple and effective 
# way to check whether expected conditions hold true during testing.

# python
# Copy code
# def test_divide():
#     assert divide(10, 2) == 5
#     assert divide(10, 0) == 0, "Expected division by zero to return 0"

# test_divide()
# Documentation: assert statements can serve as a form of self-documentation, 
# making it explicit what assumptions or conditions the code relies on.

# python
# Copy code
# def process_data(data):
#     assert data, "Data should not be empty"
#     # Process the data
#       global
g=10
def initLizeNewValue():
    print("before initilize",g)
    # global g
    # g=12
    print("after initilize",g)
    print(g)
initLizeNewValue()

# elif
e1=2
e2=4
e3=5
if e1>e2:
    print(e1)
elif e2>e3:
    print(e2)
else:
    print("value of e3 is :",e3)