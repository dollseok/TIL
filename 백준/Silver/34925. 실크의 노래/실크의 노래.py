H, S = map(int, input().split())

if H <= 2:
    ans = 1
elif H <= 4:
    ans = 2 + S
elif H % 2 == 1:
    ans = (H + 1) // 2 + (3 * S) // 2
else:
    ans = H // 2 + (3 * S + 1) // 2

print(ans)