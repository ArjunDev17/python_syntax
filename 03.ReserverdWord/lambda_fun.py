# normal function
def add(number1,number2):
    return number1+number2
result =add(2,3)
print("sumition of two number is :",result)

# anonymas function (Lambda function)

add=lambda x,y:x+y
result=add(4,7)
print(result)

#----------------------------------------------
# case :1 Passing Functions as Arguments

def sumOfTwo(x,y,addition):
    return addition(x,y)

addition=lambda x,y:x+y

result =sumOfTwo(10,12,addition)
print("sum by lambda",result)

# case 2 Mapping and Filtering:
numbers=[2,4,6]
addition=lambda x,y:x+y
result =list(map(lambda x:x**2,numbers))
print("sum by lambda",result)

