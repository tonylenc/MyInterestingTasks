res = set()


def func(n, seq):
    if len(seq) == n:
        global res
        res.add(seq)
    else:
        cur_n = len(seq)
        not_allowed = set()

        for i in range(len(seq)):
            not_allowed.add(seq[i])
            not_allowed.add(seq[i] + cur_n - i)
            not_allowed.add(seq[i] - cur_n + i)

        options = set(range(n)) - not_allowed

        for i in options:
            func(n, seq + (i,))


n = int(input())
func(n, ())
cnt = 0

for i in res:
    print(cnt + 1)
    print()
    for a in range(n):
        cur = [0] * n
        cur[i[a]] = 1
        print(*cur)
    print()
    cnt += 1
