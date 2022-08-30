n = int(input())
graph = {}
were = set()

for _ in range(n):
    a, b = map(int, input().split())
    graph[a] = b
    graph[b] = a

stack = {1}  # first el

while stack:
    cur = stack.pop()

    for i in graph[cur]:
        if i in were:
            pass
        else:
            stack.add(i)

    were.add(cur)
