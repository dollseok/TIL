'''
20529번 가장 가까운 세사람의 심리적 거리

풀이

16가지의 MBTI 유형
한글자 다르면 거리 = 1 (ex) ISTJ, ISFJ = 1 / INTP, ENTJ = 2
a,b,c 세사람의 심리적 거리 = a,b + b,c + c,a

세사람 골라서 심리 거리 구하면 되는데 최솟값이 나오는 세사람을 골라야한다.
전체 리스트에서 3사람만 구하는 방법
- 조합으로 전체에서 3 => 당연히 시간 초과

16*16 arr를 만들어서 각 mbti를 index 딕셔너리를 만든 후에
세개씩 골라서 최소값

만약 같은게 3개 이상 있다면 결과값은 0


'''
from itertools import combinations

def select_three(lst,n):
    combi = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                combi.append((lst[i],lst[j],lst[k]))
    return combi

def checkDistance(m1,m2):
    cnt = 0
    for i in range(4):
        if m1[i] != m2[i]:
            cnt += 1
    return cnt

tc = int(input())
INF = 10e9
for _ in range(tc):
    result = INF
    n = int(input())
    mbti = list(input().split())
    if n >= 33:
        print(0)
        continue
    combi_list = combinations(mbti,3)
    for data in combi_list:
        dist = checkDistance(data[0],data[1]) + checkDistance(data[1],data[2]) + checkDistance(data[0],data[2])
        result = min(dist,result)
    print(result)