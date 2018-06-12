import numpy as np


np.random.seed(444)

N = 10000
sigma = 0.1
noise = sigma * np.random.randn(N)
x = np.linspace(0, 2, N)
d = 3 + 2 * x + noise
d.shape = (N, 1)

# We need to prepend a column vector of 1s to `x`.
X = np.column_stack((np.ones(N, dtype=x.dtype), x))


squares = [x * x for x in range(10) if x > 5]
print(squares)

# Dictionary and Set comprehensions
functions = {"add": (lambda x, y: x + y),
             "sub": (lambda x, y: x - y),
             "mul": (lambda x, y: x * y),
             "div": (lambda x, y: x / y),}


def operation(operator, x, y):
    return functions.get(operator, lambda: None)(x, y)


print(operation("mul", 2, 2))
