def solution(s):
    
    l = list(s)
    
    d = dict()
    answer = []
    
    for i in range(len(l)):
        # print(d)
        w = l[i]
        
        if w not in d:
            answer.append(-1)
        else:
            answer.append(i - d[w])
        
        d[w] = i
    
    return answer