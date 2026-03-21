# A
a1 = int(input())
b1 = int(input())

for i in range(a1, b1 + 1):
    if i % 2 == 0:
        print(i, end=" ")

# B
a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")

# C
a2 = int(input())
b2 = int(input())
for i in range(a2, b2 + 1):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=" ")

# D
x1 = input()
d1 = input()
print(x1.count(d1))

# E
x = input()
s = 0
for d2 in x:
    s += int(d2)
print(s)

# F
x3 = input()
print(int(x3[::-1]))

# G
y = int(input())
for i in range(2, y + 1):
    if y % i == 0:
        print(i)
        break

# H
h = int(input())
for i in range(1, h + 1):
    if h % i == 0:
        print(i, end=" ")

# I
h = int(input())
count = 0
for i in range(1, h + 1):
    if h % i == 0:
        count+= 1
print(count)

# J
j = 0
for i in range(100):
    x = int(input())
    j += x
print(s)

# K
k = int(input())
s1 = 0
for i in range(k):
    x = int(input())
    s1 += x
print(s1)

#L
l = input()
print(int(l, 2))

#M
m = int(input())
count = 0
for i in range(m):
    m = int(input())
    if m == 0:
        count += 1
print(count)