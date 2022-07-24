n, m = map(int, input().split())
seq = [[0 for _ in range(m)] for _ in range(n)]
cnt = 1

i = 0
j = 0

while m * n > cnt:
    while j < m - 1 and seq[i][j + 1] == 0:
        seq[i][j] = cnt
        cnt += 1
        j += 1
    while i < n - 1 and seq[i + 1][j] == 0:
        seq[i][j] = cnt
        cnt += 1
        i += 1
    while j > 0 and seq[i][j - 1] == 0:
        seq[i][j] = cnt
        cnt += 1
        j -= 1
    while i > 0 and seq[i - 1][j] == 0:
        seq[i][j] = cnt
        cnt += 1
        i -= 1

seq[i][j] = cnt

for i in seq:
    for j in i:
        print(str(j).ljust(3), end='')
    print()
