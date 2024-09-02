'''

수열 S에서 최대 K번 원소를 삭제한 수열에서 짝수로 이루어져있는 연속된 부분의 수열의 가장 긴 길이

i = 0
j = 0 에서 시작

K번 삭제를 최대로 사용하는게 좋음
홀수인거를 삭제하는게 좋다

'''

n,k = map(int,input().split())
ls = list(map(int,input().split()))

i = 0
j = 0
length = 0
delete_cnt = 0
result = 0

while j < n:
    if ls[j] % 2 == 0: # 짝수일 때
        length += 1
        j += 1
    else:
        if delete_cnt < k: # 삭제 할수 있는 상황
            length += 1
            delete_cnt += 1
            j += 1
        else: # 삭제 불가인 상황
            if ls[i] % 2 == 0: # 가장 앞에것이 짝수일 때
                length -= 1
                i += 1
            else:
                length -= 1
                delete_cnt -= 1
                i += 1

    result = max(result,length)

print(result - delete_cnt)