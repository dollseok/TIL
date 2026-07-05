def solution(a, b, n):
    answer = 0
    while n >= a:
        cola = (n // a) * b
        remain = n % a
        answer += cola
        n = remain + cola
    
    return answer