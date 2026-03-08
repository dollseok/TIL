n = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

r = 0
for i in range(n):
    r += A[i] * B[i]

print(r)