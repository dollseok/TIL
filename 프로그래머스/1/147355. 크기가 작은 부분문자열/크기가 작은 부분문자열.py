def solution(t, p):
    l = len(p)
    result = 0
    for i in range(len(t) - l + 1):
        lst = list(t)
        if int(''.join(lst[i:i+l])) <= int(p):
            result += 1 
        
    return result