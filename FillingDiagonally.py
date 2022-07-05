width, height = map(int, input().split())

cnt = 1
arr = [[0 for w in range(width)] for h in range(height)]

for diag in range(width + height):
    for h in range(height):
        for w in range(width):
            if w + h == diag - 1:
                arr[h][w] = str(cnt).ljust(len(str(width * height)))
                cnt += 1

for i in arr:
    print(*i)
