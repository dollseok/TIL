def solution(n):
    result = set()
    for i in range(1, n+1):
        if n % i == 0:
            result.add(i)
    answer = sum(list(result))
    return answer