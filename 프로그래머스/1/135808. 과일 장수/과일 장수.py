def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    l = len(score)
    lst = []
    i = 0
    while l != 0:
        lst.append(score[i])
        i += 1
        l -= 1
        if len(lst) == m:
            answer += min(lst) * m
            lst = []
        
    return answer