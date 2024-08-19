'''
N 최대 1000명의 인원수

임의의 한명을 골랐을 때 그와 같은 수의 사람을 모두 뺀다
그렇게했을 때 연속하는 숫자가 가장 긴 것
용량은 0 ~ 1000000

모두 달라도 경우의 수는 N개까지만 나올 수있음
최대 1000개 / 1000사이즈의 리스트를 돌려서 돌려서 사람 뺀 후에 / 1000사이즈의 리스트 그안에 최장 길이의 연속된 수를 구하면
1 000 000 000 => 10억 => 불가능

사이즈를 줄이는 파트가 필요함
- 미리 다 빼는 것이 아니라 종류 set() 안에서 한번씩 빼보고 가장 긴 리스트 체크
1000개 * 1000사이즈
5
0
1
0
1
0
'''

N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

set_arr = set(arr)

result = 0
for i in list(set_arr):
    cnt = 1
    before_num = arr[0]
    for j in range(1,N):
        if arr[j] == i:
            continue

        if before_num == arr[j]:
            cnt += 1
        else:
            before_num = arr[j]
            cnt = 1

        result = max(result, cnt)


print(result)