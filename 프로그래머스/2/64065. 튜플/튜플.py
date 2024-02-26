'''
s: 5-1000000이하
문자열로 들어오는 걸 나눈다
},{ 이거 기준으로 나누면
'''
from collections import deque

def solution(s):
    s = s[2:-2]
    arr = list(s.split('},{'))
    result = [] # 순서대로 데이터를 담을 것
    arr.sort(key=len)
    tuple_list = []
    cnt = 0
    for tuple in arr:
        tuple_list.append(list(map(int,tuple.split(','))))
        cnt += 1
    
    dict = {}
    for i in tuple_list[-1]:
        dict[i] = 0

    order = 1
    for tuple in tuple_list:
        for i in tuple:
            if dict[i] == 0:
                dict[i] = order
        order += 1
    
    # 딕셔너리 value값 큰순서로 정렬
    d1 = sorted(dict.items(), key=lambda x: x[1])

    for i in d1:
        result.append(i[0])
    
    answer = result
    return answer