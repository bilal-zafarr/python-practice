#---------

'''
abs()
returns the absolute value of a number
'''
print(abs(-5)) 

print("----------")
#----------

'''
all()
return true if all items in a iterable are true
'''

mylist = [True, True, True]
print(all(mylist))

mylist = [True, 0, True]
print(all(mylist))

print("----------")
#----------

'''
any()
return true if any item in a iterable are true
'''

mylist = [True, True, True]
print(any(mylist))

mylist = [True, 0, True]
print(any(mylist))

print("----------")
#----------

'''
The ascii() function returns a readable version of any object (Strings, Tuples, Lists, etc).
The ascii() function will replace any non-ascii characters with escape characters:
'''

print(ascii("My name is Ståle"))

print("----------")
#----------

'''
The bin() function returns the binary version of a specified integer.
The result will always start with the prefix 0b.
'''

print(bin(5))

print("----------")
#----------

'''
The bool() function returns the boolean value of a specified object.
'''

print(bool("Any String"))
print(bool([]))

print("----------")
#----------

'''
The bytearray() function returns a bytearray object.
It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
'''

print(bytearray(4))

print("----------")
#----------

'''
The bytes() function returns a bytes object.
It can convert objects into bytes objects, or create empty bytes object of the specified size.
'''

print(bytes(4))

print("----------")
#----------

'''
The callable() function returns True if the specified object is callable, otherwise it returns False.
'''

print(callable(5))

print("----------")
#----------

'''
The chr() function returns the character that represents the specified unicode.
'''

print(chr(99))

print("----------")
#----------

'''
The classmethod() method returns a class method for the given function. ########################
'''

print("----------")
#----------

'''
The compile() function returns the specified source as a code object, ready to be executed.
'''

code = compile('print(55)', 'test', 'eval')
exec(code)

print("----------")
#----------


'''
The complex() function returns a complex number by specifying a real number and an imaginary number.
'''

print(complex(3, 5))

print("----------")
#----------

'''
The delattr() function will delete the specified attribute from the specified object.
'''

class Person:
  name = "John"
  age = 36
  country = "Norway"

delattr(Person, 'age')
print(dir(Person))

print("----------")
#----------

'''
The dict() function creates a dictionary.
'''

print(dict(name = "John", age = 36, country = "Norway"))

print("----------")
#----------

'''
The dir() function returns all properties and methods of the specified object, without the values.
'''

print(dir(Person))

print("----------")
#----------

'''
The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
'''

print(divmod(5, 2))

print("----------")
#----------

'''
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
'''

x = ('apple', 'banana', 'cherry')
print(list(enumerate(x)))

print("----------")
#----------

'''
The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
'''

x = 'print(55)'
eval(x)

print("----------")
#----------

'''
The exec() function executes the specified Python code.
'''

x = 'name = "John"\nprint(name)'
exec(x)

print("----------")
#----------

'''
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
'''

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if (x > 18): return True
  else: return False

adults = filter(myFunc, ages)
print(list(adults))

print("----------")
#----------

'''
The float() function converts the specified value into a floating point number.
'''

print(float(3))

print("----------")
#----------

'''
The format() function formats a specified value into a specified format.
'''

print(format(0.5, '%'))

print("----------")
#----------

'''
The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
'''

mylist = ['apple', 'banana', 'cherry']
x = print(frozenset(mylist))

print("----------")
#----------

'''
The getattr() function returns the value of the specified attribute from the specified object.
'''

class Person:
  name = "John"
  age = 36
  country = "Norway"

print(getattr(Person, 'age'))

print("----------")
#----------

'''
The globals() function returns the global symbol table as a dictionary.
'''

print(globals())

print("----------")
#----------

'''
The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
'''

print(hasattr(Person, "age"))

print("----------")
#----------

'''
hash()	Returns the hash value of a specified object
'''

print(hash("This is my string"))

print("----------")
#----------

'''
help()	Executes the built-in help system
'''

####help(print)

print("----------")
#----------

'''
The hex() function converts the specified number into a hexadecimal value.
'''

print(hex(13))

print("----------")
#----------

'''
The id() function returns a unique id for the specified object.
'''

x = 10
print(id(x))

print("----------")
#----------

'''
The input() function allows user input.
'''

####x = input()

print("----------")
#----------

'''
The int() function converts the specified value into an integer number.
'''

print(int(3.5))

print("----------")
#----------

'''
The isinstance() function returns True if the specified object is of the specified type, otherwise False.
'''

print(isinstance(3.5, float))

print("----------")
#----------

'''
The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
'''

class A:
    age = 21

class B(A):
    age = 22

print(issubclass(B, A))

print("----------")
#----------

'''
The iter() function returns an iterator object.
'''

x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

print("----------")
#----------

'''
The len() function returns the number of items in an object.
'''

print(len("My String"))

print("----------")
#----------

'''
The list() function creates a list object.
'''

print(list((1, 5, 9)))

print("----------")
#----------

'''
The locals() function returns the local symbol table as a dictionary.
'''

print(locals())

print("----------")
#----------

'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
'''

def myfunc(n):
  return len(n)

print(list(map(myfunc, ('apple', 'banana', 'cherry'))))

print("----------")
#----------

'''
The max() function returns the item with the highest value, or the item with the highest value in an iterable.
'''

print(max(5, 10))

print("----------")
#----------

'''
The memoryview() function returns a memory view object from a specified object.
'''

x = memoryview(b"Hello")

print(x)

print("----------")
#----------

'''
The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
'''

print(min(5, 10))

print("----------")
#----------

'''
The next() function returns the next item in an iterator.
'''

mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))
print(next(mylist))

print("----------")
#----------

'''
The next() function returns the next item in an iterator.
'''

mylist = iter(["apple", "banana", "cherry"])
print(next(mylist))
print(next(mylist))

print("----------")
#----------

'''
The object() function returns an empty object. A base object for all the objects
'''

print(object())

print("----------")
#----------

'''
The oct() function converts an integer into an octal string.
'''

print(oct(10))

print("----------")
#----------

'''
The open() function opens a file, and returns it as a file object.
'''

#f = open("demofile.txt", "r")

print("----------")
#----------

'''
The ord() function returns the number representing the unicode code of a specified character.
'''

print(ord("h"))

print("----------")
#----------

'''
The pow() function returns the value of x to the power of y
'''

print(pow(2, 5))

print("----------")
#----------

'''
The print() function prints the specified message to the screen, or other standard output device.
'''

print("The print() function")

print("----------")
#----------

'''
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
'''

print(range(5))

print("----------")
#----------

'''
The reversed() function returns a reversed iterator object.
'''

alph = ["a", "b", "c", "d"]
print(list(reversed(alph)))

print("----------")
#----------

'''
The round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.
'''

print(round(5.76543, 2))

print("----------")
#----------

'''
The set() function creates a set object.
'''

print(set(('apple', 'banana', 'cherry')))

print("----------")
#----------

'''
The setattr() function sets the value of the specified attribute of the specified object.
'''

class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

print(Person.age)

print("----------")
#----------

'''
The slice() function returns a slice object.
'''

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

print("----------")
#----------

'''
The slice() function returns a slice object.
'''

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 3)
print(a[x])

print("----------")
#----------

'''
The sorted() function returns a sorted list of the specified iterable object.
'''

a = ("b", "g", "a", "d", "f", "c", "h", "e")
print(sorted(a))

print("----------")
#----------

'''
The str() function converts the specified value into a string.
'''

print(str(3.5))

print("----------")
#----------

'''
The sum() function returns a number, the sum of all items in an iterable.
'''

a = (1, 2, 3, 4, 5)
print(sum(a))

print("----------")
#----------

'''
The super() function is used to give access to methods and properties of a parent or sibling class.
The super() function returns an object that represents the parent class.
'''

#----------

'''
The tuple() function creates a tuple object.
'''

print(tuple(('apple', 'banana', 'cherry')))

print("----------")
#----------

'''
The type() function returns the type of the specified object
'''

print(type(3))

print("----------")
#----------

'''
The vars() function returns the __dic__ attribute of an object.
'''

class Person:
  name = "John"
  age = 36
  country = "norway"

print(vars(Person))
print("----------")
#----------

'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
and then the second item in each passed iterator are paired together etc.
'''

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Bill")

print(list(zip(a, b)))
print("----------")
#----------