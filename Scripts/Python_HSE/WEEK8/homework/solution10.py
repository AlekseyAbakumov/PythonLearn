from functools import reduce
from operator import xor

print(
    *reduce(
        lambda x, y: map(xor, x, y),
        map(
            lambda line: map(
                int,
                line.split()
            ),
            map(
                lambda _: input(),
                range(
                    int(
                        input()
                    )
                )
            )
        )
    )
)
