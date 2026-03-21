#A
def min4(a, b, c, d):
    return min(a,b,c,d)
a, b, c, d = map(int, input().split())
print(min4(a, b, c, d))

#B
def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result
a, n = input().split()
a = float(a)
n = int(n)
print(power(a, n))

#C
def xor(x, y):
    if (x and not y) or (not x and y):
        return 1
    return 0
x, y = map(int, input().split())
print(xor(bool(x), bool(y)))





