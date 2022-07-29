#basic types
x = 3 # int immutable
x = 3.5 # float immutable
x = (1, 2, 3) # tuple immutable
x = [1,2,3] # list mutable
x = {"key": "value"} # dict mutable
x = {1, 2, 3} # set mutable

# Only immutable objects can be keys of a dict
# check type with
print(type(x))

# add key to dictionary
x["key2"] = "value2" #todo: fix this

# How sets work
a = {'ciao'}
a.add('hello')
print(a) # {'ciao', 'hello'}
a.add('hello')
print(a) # {'ciao', 'hello'}

# Set list use case
mylist = ["hey", "hello", "hi", "how", "are", "you", "today", "today", "today"]
mylist = list(set(mylist)) # remove duplicates
print(mylist) # ['hey', 'hello', 'hi', 'how', 'are', 'you', 'today']

# Check if collection contains an element
print("hey" in mylist) # True

# Also works with tuples, lists, dicts, sets
print((1,2,3) in mylist) # False
  
#check if collection is empty
print(len(mylist) == 0) # False
