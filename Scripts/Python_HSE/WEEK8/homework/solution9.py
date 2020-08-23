import itertools

print(
    *map(
        ''.join,
        itertools.permutations(
            ''.join(
                map(
                    str,
                    list(
                        range(
                            1,
                            int(
                                input()
                            ) + 1
                        )
                    )
                )
            )
        )
    ),
    sep='\n'
)
