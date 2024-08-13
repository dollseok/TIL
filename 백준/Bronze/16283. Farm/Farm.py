'''

a 1000,b 1000,n 1000,w 1000000
양은 a 그램 염소는 b그램
하루동안 소비한 전체 사료의 양만 확인해서 양과 염소의 각 몇마리인지 확인
두마리 합 n 마리, 소비한 사료 w 그램

가능한 해가 두개 이상 or 가능한 해가 없으면 -1 출력

1. 전체 n마리 양을 1마리부터 n마리까지 늘려가며 확인 => 많아봣자 1000 0.1 초면 1000만 게산 충분

2. 수학적으로 a*양 b*염소 = w / 양+염소 = n 공식으로 확인

'''

a,b,n,w = map(int,input().split())

cnt = 0
result = 0
for i in range(1,n):
    if a * i + b*(n-i) == w:
        cnt += 1
        result = i

if cnt == 1:
    print(result, n-result)
else:
    print(-1)