def solution(s):
    lst = list(s)
    l =len(lst)
    answer = ''
    if l % 2:
        answer = lst[l // 2]
    else:
        answer = lst[l//2 - 1] + lst[l//2]
    
    return answer