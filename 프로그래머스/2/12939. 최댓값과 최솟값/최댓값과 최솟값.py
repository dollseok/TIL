def solution(s):
    lst = list(map(int,s.split(" ")))
    answer = f"{min(lst)} {max(lst)}"
    
    return answer