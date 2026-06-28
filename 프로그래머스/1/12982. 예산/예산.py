def solution(d, budget):
    answer = 0
    newl = sorted(d)
    print(newl)
    n = 0
    for i in newl:
        if n + i > budget:
            return answer
        else:
            n += i
            answer += 1
    
    return answer