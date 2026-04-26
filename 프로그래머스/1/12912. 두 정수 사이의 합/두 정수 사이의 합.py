def solution(a, b):
    answer = 0
    end = max(a,b)
    start = min(a,b)
    
    for i in range (start,end+1):
        answer += i
    
    return answer