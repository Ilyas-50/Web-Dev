# A
aa = int(input())
ba = int(input())
print(max(aa, ba))


# B
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("YES")
else:
    print("NO")


# C
a = int(input())
b = int(input())

if (a == 1 and b == 1) or (a != 1 and b != 1):
    print("YES")
else:
    print("NO")


# D 
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)


# E
ab = int(input())
bb = int(input())
if ab > bb:
    print(1)
elif bb > ab:
    print(2)
else:
    print(0)