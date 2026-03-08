n, m = map(int, input().split())
d = int(input())

ans = 0

for i in range(n):
    for j in range(m):
        d1 = i + j
        d2 = i + (m - 1 - j)
        d3 = (n - 1 - i) + j
        d4 = (n - 1 - i) + (m - 1 - j)

        if max(d1, d2, d3, d4) < d:
            ans += 1

print(ans)