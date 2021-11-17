def prog(n: int = 10, denominator: int = 2):
    next_number = 1
    index = 1
    while index < n:
        yield f'{next_number} ({denominator=})'
        next_number = next_number * denominator
        index += 1
    return


a = prog(7, 5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))