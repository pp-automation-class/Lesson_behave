# Import math Library
import math


# # Return the base-2 logarithm of different numbers
# print(math.log2(2.7183))
# print(math.log2(2))
# print(math.log2(1))


def pip(a: float, b: float) -> float:
    if a <= 0:
        raise ValueError("a must be > 0 for log2(a)")
    return 2 ** (b * math.log2(a))


x = 1.022393
print(x)
print(pip(2, x))
print(pip(x, 32))
print("\n")

x: float = 1
precision: float = 1.0e-9
while x < 2:
    left = 2**x
    right = x**32
    if (left - right) < precision:
        break
    x += precision


print(x)
print(2**x)
print(x**32)
