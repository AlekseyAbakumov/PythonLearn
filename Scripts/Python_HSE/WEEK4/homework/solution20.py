def reverseSequense():
    n = int(input())
    if n != 0:
        reverseSequense()
        print(n)
    if n == 0:
        print(0)


reverseSequense()
