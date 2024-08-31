'''
N개 종류의 알파벳을 가진 연속된 문자열 밖에 인식
이 번역기가 인식할 수 있는 최대 문자열의 길이

알파벳의 종류 N개 인식 가능
인식할수 있는 최대 문자열 길이

abcdef ghijk lmnop qrstu vwxyz

완전탐색

combi는 위험, 26개중에 13개 고르는게 최대일듯 => 근데 이거도 엄청 큼

처음부터 탐색하면서 그 길이까지의 같은 단어 개수 cnt => 딕셔너리로 각 단어 관리
길이 length

'''

target = int(input())

ls = list(input())

n = len(ls)

alpha = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
length = 1
cnt = 1
alpha[ls[0]] = 1

i = 0
j = 0
result = 0

while j < n:

    if cnt <= target:
        result = max(result,length)
        if j == n-1:
            break

        j += 1
        if alpha[ls[j]] == 0:
            cnt += 1
        length += 1
        alpha[ls[j]] += 1
    elif cnt > target:
        alpha[ls[i]] -= 1
        if alpha[ls[i]] == 0:
            cnt -= 1
        length -= 1
        i += 1


print(result)


'''
2
aaaaaaaaa


'''