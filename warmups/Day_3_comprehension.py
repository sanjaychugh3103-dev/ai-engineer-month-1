# List comprehension
squares = [x*x for x in range(10)]    
print(squares)

# Dictionary comprehension
lookup  = {x: x*x for x in range(10)}     
print(lookup)

# Set comprehension
evens = {x for x in range(20) if x % 2 == 0}
print(evens)

squares_gen = (x*x for x in range(10))   # note the parentheses, not brackets
print(squares_gen)  # This will print a generator object
print(list(squares_gen))  # This will print the list of squares