import numpy as np

x = np.array([1, 2, 3, 4], dtype=np.int64)

print(x)
print(x.dtype)
print(x.shape)

print(x[1])
print(x[0])

m = np.array([[2, 3, 4], [5, 6, 7]])
print(m)
print(m.shape)
print(m[1, 2])

y = np.ones(5)
print(y)
y = np.zeros(5)
print(y)

z = np.eye(6)
print(z)

i = np.random.random((2, 3))
print(i)
