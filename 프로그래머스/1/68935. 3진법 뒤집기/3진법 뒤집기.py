def solution(n):
    
    n3 = []
    
    while True:
        if n == 0:
            break    
        n3.append(n % 3)
        n = n // 3
    
    answer = 0
    for i in range(len(n3)):
        answer += n3[len(n3) - 1 - i] * (3**i)
    
    return answer