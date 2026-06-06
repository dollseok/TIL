def count_divisor(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    
    return cnt

def solution(left, right):
    result = 0
    for num in range(left,right+1):
        cnt = count_divisor(num)
        
        if cnt % 2 == 0:
            result += num
        else:
            result -= num
    
    return result