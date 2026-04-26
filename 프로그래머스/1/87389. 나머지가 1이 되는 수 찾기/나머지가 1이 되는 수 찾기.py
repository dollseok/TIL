def solution(n):
    answer = 0
    
    num = 1
    while True:
        if n % num == 1:
            answer = num
            break
        
        num += 1
    
    
    return answer