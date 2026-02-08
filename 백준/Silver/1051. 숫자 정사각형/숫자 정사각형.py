N,M = map(int, input().split())

arr = [list(input()) for _ in range(N)]


def solve():
    max_side = min(N, M)

    for side in range(max_side, 0, -1):
        d = side - 1
        for i in range(N - d):
            for j in range(M - d):            
                v = arr[i][j]
                if v == arr[i][j+d] and v == arr[i+d][j] and v == arr[i+d][j+d]:
                    return side * side
    return 1

print(solve())