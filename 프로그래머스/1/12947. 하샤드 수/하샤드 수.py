def solution(x):
    answer = True
    hashad = sum(map(int,list(str(x)))) 
    if x % hashad != 0:
        answer = False    

    return answer