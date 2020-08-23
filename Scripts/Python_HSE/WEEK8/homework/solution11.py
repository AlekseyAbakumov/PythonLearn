from math import sqrt

print(
    *map(
        lambda s:
        s[0],
        filter(
            lambda x:
            x[0] * x[1],
            map(
                lambda a:
                (
                    a,
                    all(
                        map(
                            lambda x:
                            a % x,
                            map(
                                int,
                                range(
                                    2,
                                    int(
                                        sqrt(a) + 1
                                    )
                                )
                            )
                        )
                    )
                ),
                map(
                    int,
                    range(
                        2,
                        int(input()) + 1)
                )
            )
        )
    )
)
