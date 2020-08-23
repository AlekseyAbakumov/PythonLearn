import itertools

print(
    *itertools.accumulate(
        [1] + list(range(1, int(input()) + 1)),
        lambda x, y: x * y
    )
)
