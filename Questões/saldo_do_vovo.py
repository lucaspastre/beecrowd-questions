n, s = map(int, input().split())
m = s
for i in range(0, n):
    a = int(input())
    s += a
    if s < m:
        m = s

print(m)
