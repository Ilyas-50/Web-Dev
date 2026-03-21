# 1
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if i%2 == 0:
        print(arr[i], end = ' ')

# 2
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    if arr[i]%2 == 0:
        print(arr[i], end = ' ')

# 3
n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    if arr[i]> 0:
        print(sum)

# 4
n = int(input())
arr = list(map(int, input().split()))
sum = 0
for i in range(n):
    if(i > 0):
        if arr[i]> arr[i-1]:
            sum += 1
print(sum)

# 5
n = int(input())
arr = list(map(int, input().split()))
have = False
for i in range(1, n):
    if arr[i] * arr[i-1] > 0:
        have = True
if have:
    print("YES")
else:
    print("NO")

# 6
n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        count += 1
print(count)

# 7
n = int(input())
arr = list(map(int, input().split()))
# for i in range(n):
for i in arr[::-1]:
    print(i, end = " ")