def solution(n):
    l = list(str(n))
    answer = []
    for i in range(len(l) - 1,-1,-1):
        answer.append(int(l[i]))
    
    return answer