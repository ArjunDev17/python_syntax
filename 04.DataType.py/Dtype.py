int
float
complex
bool
str
bytes
bytearray
range
list
tuple
set 
frozenset
dict
None

i=10
print(type(i))

f=10.4
print(type(f))

z=3+4j
z1=complex(2,5)
print(z)
print(z1)

# byte
data=b'ramji'
print("it is byte form :",data)
print(type(data))

lst=[2,4,6]
print(type(lst))

tup=(2,4,6)
print(type(tup))

sets={2,4,6}
print(type(sets))

print(id(sets))

# frozenset: Represents immutable collections of unique items.

my_frozenset = frozenset({1, 2, 3, 4})
# Use Case: Similar to set, but when you need an immutable version of the collection.

# dict: Represents collections of key-value pairs.
vocab={'name':'fakeX'}
print(type(vocab))


