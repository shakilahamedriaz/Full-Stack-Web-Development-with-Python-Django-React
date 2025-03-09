"""Tuple in Python
A tuple is an ordered, immutable (unchangeable) collection in Python,
 meaning its elements cannot be modified after creation. It is often
  used for data that should remain constant"""

#touple() --> Immutable
# Using parentheses ()
my_tuple = (1, 2, 3, "Python", 4.5)

# Without parentheses (Implicit tuple)
another_tuple = 1, 2, 3, "AI", 5.6

# Empty tuple
empty_tuple = ()

# Single-element tuple (comma is required)
single_element_tuple = (10,)  # ✅ Correct
not_a_tuple = (10)  # ❌ This is just an integer, not a tuple

print(type(single_element_tuple))  # Output: <class 'tuple'>
print(type(not_a_tuple))  # Output: <class 'int'>
  

t = (1, 2, 3)
#t[0] = 100
#print(t)
#TypeError: 'tuple' object does not support item assignment


t_r = (reversed(t))
print(t)
print(t_r)