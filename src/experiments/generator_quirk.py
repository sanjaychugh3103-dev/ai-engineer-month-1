gen = (x*x for x in range(5))

print("first pass:")
for v in gen:
    print(v)

print("second pass:")
for v in gen:
    print(v)