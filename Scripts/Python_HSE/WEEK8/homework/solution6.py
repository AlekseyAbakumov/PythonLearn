print(
    *map(
        lambda x, y: x ^ y,
        list(
            map(
                int,
                input().split()
            )
        ),
        list(
            map(
                int,
                input().split()
            )
        )
    )
)
