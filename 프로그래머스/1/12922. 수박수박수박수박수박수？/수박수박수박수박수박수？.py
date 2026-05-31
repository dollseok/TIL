def solution(n):
    st = "수박" * 6000
    lst = list(st)
    answer = "".join(lst[:n])
    return answer