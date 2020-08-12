def takeDisk(height, fp, tp):
    print(height, fp, tp)


def takeTower(height, fromPole, toPole, withPole):
    if height >= 1:
        takeTower(height - 1, fromPole, withPole, toPole)
        takeDisk(height, fromPole, toPole)
        takeTower(height - 1, withPole, toPole, fromPole)


n = int(input())
takeTower(n, 1, 3, 2)
