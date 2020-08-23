import itertools

print(
    *itertools.accumulate(
        list(
            map(
                int,
                input().split()
            )
        )
    )
)
