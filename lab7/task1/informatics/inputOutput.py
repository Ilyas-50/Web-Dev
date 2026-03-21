import math

# A
a = int(input())
b = int(input())
c = math.sqrt(a**2 + b**2)
print(c)


# B
n = int(input())
print("the next number for the number", n, "is", n + 1, sep=" ", end=".\n")
print("the previous number for the number", n, "is", n - 1, sep=" ", end=".")


#  C
n1 = int(input())
k = int(input())
print(k // n1)


# D
n2 = int(input())
k2 = int(input())
print(k2 % n2)


# E
v = int(input())
t = int(input())

print((v * t) % 109)
