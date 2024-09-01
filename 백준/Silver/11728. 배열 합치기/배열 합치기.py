'''

정렬되어있는 두 배열 A,B
두배열 합쳐서 정렬해서 출력하는 프로그램

'''
n,m = map(int,input().split())

a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

i = 0
j = 0

arr = []
while i < n and j < m:
    if a_list[i] <= b_list[j]:
        arr.append(a_list[i])
        i += 1
    elif a_list[i] > b_list[j]:
        arr.append(b_list[j])
        j += 1

if i == n: # a리스트가 끝까지 도착했을 때
    while j < m:
        arr.append(b_list[j])
        j += 1

elif j == m: # b리스트가 끝까지 도착햇을 때
    while i < n:
        arr.append(a_list[i])
        i += 1

print(*arr)


