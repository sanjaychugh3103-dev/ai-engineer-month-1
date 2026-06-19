from collections import Counter
numbers = [1,2,3,4,5]
freq=Counter(numbers)
print(freq) 
result = any(v > 1 for v in freq.values())
print(result)  # True