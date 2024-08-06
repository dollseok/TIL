A,B = map(int,input().split())
result = []

for i in range(-2000,2001):
    if i*i + 2*A*i + B == 0:
        result.append(i)

print(*result)
