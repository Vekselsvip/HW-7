def my_range(start: int = 0, stop: int = 10, step: int = 1,):
    while start <= stop:
        yield start
        start += step


x = my_range(0, 50, 5)
print(next(x))
print(next(x))
print(next(x))
