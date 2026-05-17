def solution(num):
    
    cnt = 0
    if num == 1:
        return 0
    while True:
        cnt += 1
        if num % 2 == 0: # 짝수
            num = num // 2
            
        else:
            num = num * 3 + 1
        
        if num == 1:
            return cnt
        
        if cnt == 500:
            return -1
            break
