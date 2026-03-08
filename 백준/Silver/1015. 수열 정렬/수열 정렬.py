N = int(input())

A = list(map(int,input().split()))

arr = []
for i in range(N):
    arr.append((A[i], i))

arr.sort()

P = [0] * N

for sorted_idx, (_, original_idx) in enumerate(arr):
    P[original_idx] = sorted_idx


print(*P)
