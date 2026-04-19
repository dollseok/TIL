import math
def solution(n):
    answer = 0
    if float(math.sqrt(n).is_integer()):
        answer = (n ** 0.5 + 1) ** 2
    else:
        answer = -1
    
    return answer