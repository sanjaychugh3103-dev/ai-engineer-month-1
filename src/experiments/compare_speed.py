import time

start = time.perf_counter()
big_list = [x*x for x in range(10_000_000)]
first_5_list = sum(big_list[:5])
print(f"list took   {time.perf_counter() - start:.3f}s, first 5 sum: {first_5_list}")

start = time.perf_counter()
big_gen = (x*x for x in range(10_000_000))
first_5_gen = sum(next(big_gen) for _ in range(5))
print(f"gen took    {time.perf_counter() - start:.3f}s, first 5 sum: {first_5_gen}")