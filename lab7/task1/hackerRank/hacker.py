import math
from itertools import product

# 1 is leap
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# 2 lists
n = int(input())
arr = []
for _ in range(n):
    cmd = input().split()

    if cmd[0] == "insert":
        i = int(cmd[1])
        e = int(cmd[2])
        arr.insert(i, e)

    elif cmd[0] == "print":
        print(arr)

    elif cmd[0] == "remove":
        e = int(cmd[1])
        arr.remove(e)

    elif cmd[0] == "append":
        e = int(cmd[1])
        arr.append(e)

    elif cmd[0] == "sort":
        arr.sort()

    elif cmd[0] == "pop":
        arr.pop()

    elif cmd[0] == "reverse":
        arr.reverse()


# 3 split_and_join
def split_and_join(line):
    g = line.split(" ")
    c = "-".join(g)
    return c

#4 set
n = int(input())
stamps = set()
for i in range(n):
    country = input()
    stamps.add(country)
print(len(stamps))


#5 power mod power
a = int(input())
b = int(input())
m = int(input())
print(pow(a, b))
print(pow(a, b, m))

# 6 list comp
def task_list_comprehensions():
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]
    print(result)


#7 itertools.product()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = product(A, B)
for pair in result:
    print(pair, end=' ')


#8. minion game
def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


# 9 no ides
def task_no_idea():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = 0
    for num in arr:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1

    print(happiness)


# 10 angle mbc
def task_find_angle():
    ab = int(input())
    bc = int(input())

    angle = math.degrees(math.atan(ab / bc))
    print(f"{round(angle)}°")
