def sumOfSequence():
    n = int(input())
    if n == 0:
        return 0
    else:
        return n + sumOfSequence()


print(sumOfSequence())
