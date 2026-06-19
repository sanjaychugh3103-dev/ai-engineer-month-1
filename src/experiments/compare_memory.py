import sys
squares_list = [x*x for x in range(10000000)]
print("list:     ", sys.getsizeof(squares_list), "bytes")

squares_gen = (x*x for x in range(10_000_000))
print("generator:", sys.getsizeof(squares_gen), "bytes")







