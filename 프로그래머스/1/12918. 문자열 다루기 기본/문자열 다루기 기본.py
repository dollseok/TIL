def solution(s):
    
    l = len(s)
    if l == 4 or l == 6:
        if s.isdigit():
            return True
    
    return False
            