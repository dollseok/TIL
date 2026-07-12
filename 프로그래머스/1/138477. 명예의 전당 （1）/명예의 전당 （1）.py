def solution(k, score):
    answer = []
    l = []
    l[:k]
    for i in score:
        l.append(i)
        l.sort(reverse=True)
        if len(l) > k:
            l.pop()
        answer.append(min(l))
    
    return answer