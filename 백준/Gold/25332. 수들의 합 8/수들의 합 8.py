'''

A수열 ,B수열
Ai~Aj = Bi~Bj  i,j(i<=j) 쌍의 개수

각 인덱스의 값이 같은 인덱스 값들을 뽑아내고 그중에 2개 뽑는 경우의 수의 개수

같은거만 하면 안됨

차이가 같은 값을 구해야함

N 200000개
i,j가 일치해야한다.
dict에 차이의 개수만큼 저장한다.

이 문제의 풀이는 같은 비율의 증가가 몇번이나 나타나는지가 메인 중점

ex)

4
1 1 3 4
4 1 4 3

prefix
0   1   2   5   9
0   4   5   9  12
0  -3  -3  -4  -3

=> -3의 비율이 이어진다.
=> 같은 비율만큼 늘어났다는 것을 의미
=> i 위치에서 그 앞에 같은 사이즈만큼 늘어난것이 몇번인지 확인하면 그만큼이 i까지에서 동일한 prefix sum 을 가지는 위치들의 개수


'''

N = int(input())
A_arr = [0] + list(map(int,input().split()))
B_arr = [0] + list(map(int,input().split()))

A_prefix = [0]*(N+1)
B_prefix = [0]*(N+1)

for i in range(1,N+1):
    A_prefix[i] = A_prefix[i - 1] + A_arr[i]
    B_prefix[i] = B_prefix[i - 1] + B_arr[i]

answer = 0
cnt = {}
for i in range(1,N+1):
    if A_prefix[i] == B_prefix[i]:
        answer += 1

    diff = A_prefix[i] - B_prefix[i]

    if diff in cnt.keys():
        answer += cnt[diff]

    if diff in cnt.keys():
        cnt[diff] += 1
    else:
        cnt[diff] = 1

print(answer)