P, X, Y = int(input()), int(input()), int(input())
print(int((X * 100 + Y) * (100 + P) / 100) // 100, ' ',
      int((X * 100 + Y) * (100 + P) / 100) % 100, sep='')
