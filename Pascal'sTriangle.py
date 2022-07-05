n = int(input())
arr = [0, 1, 0]

for i in range(n):
    arr = [0] + [arr[i] + arr[i + 1] for i in range(len(arr) - 1)] + [0]

print(arr[1:len(arr) - 1])
