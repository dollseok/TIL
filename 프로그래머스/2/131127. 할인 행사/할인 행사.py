'''
10만개의 자리에 10개씩 -> 100만 계산수 -> 가능할거같음
'''

def solution(want, number, discount):
    answer = 0
    targetdict = {}
    origindict = {}
    for i in range(len(want)):
        targetdict[want[i]] = number[i]
        
    for i in range(len(discount)-9):
        origindict = {}
        l = len(want)
        for t in range(l):
            origindict[want[t]] = 0
            
        for j in range(10):
            if discount[i+j] in want:
                origindict[discount[i+j]] += 1

        
        for k in range(l):
            if origindict[want[k]] != targetdict[want[k]]: # 중간에라도 틀리면 break
                break
            else:
                if k == len(number)-1: # 마지막 순번까지 합격이면 패스
                    answer += 1

    return answer