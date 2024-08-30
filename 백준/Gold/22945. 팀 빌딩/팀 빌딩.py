'''
A,B개발자 팀을 만들 때, 팀 능력치는

A,B 사이에 존재하는 다른 개발자 수 * min(개발자A,개발자B)

개발자수 N
N<=100000

1. 완전 탐색
두개 고르고 사이 값 구해서 결정

정렬 x

둘 사이 간격이 넓어야함 => 양끝에서 시작하면 제일 큼

거리가 넓어질수록 커진다.
1 4 2 5 3 7
i
          j  4

  i
          j  12

  i     j    8


양 끝에서 시작하면서 줄여가면 편하다
i,j 중에 작은쪽을 안쪽으로 줄여간다.


'''

N = int(input())
ls = list(map(int,input().split()))

i = 0
j = N-1
length = N - 2
result = 0
while i < j:
    result = max(result, length*(min(ls[i],ls[j])))
    if ls[i] < ls[j]:
        i += 1
        length -= 1
    elif ls[i] > ls[j]:
        j -= 1
        length -= 1
    else:
        i += 1
        j -= 1
        length -= 2

print(result)