numbers = [7,6,4,3,1]
best = None
for i, current in enumerate(numbers[:-1]):
    future_numbers = numbers[i+1:]
    best_future = max(future_numbers, key=lambda x: x - current)
    diff = best_future - current
    if best is None or diff > best[2]:
        best = (current, best_future, diff)

if best[2] <= 0:
    print(0)
else:
    print(f"Current: {best[0]}, Best Future: {best[1]}, Difference: {best[2]}")