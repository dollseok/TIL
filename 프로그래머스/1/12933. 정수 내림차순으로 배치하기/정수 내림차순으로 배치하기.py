def solution(n):
    
    answer = ''.join(sorted(list(str(n)), reverse=True))
    return int(answer)