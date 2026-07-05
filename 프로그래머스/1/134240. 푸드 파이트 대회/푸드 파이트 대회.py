def solution(food):
    
    left = ''
    right = ''
    for i in range(1,len(food)):
        cnt = food[i] // 2
        s = str(i) * cnt
        left = left + s
        right = s + right
    
    answer = left + '0' + right
    return answer