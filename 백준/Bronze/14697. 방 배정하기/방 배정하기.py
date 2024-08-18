'''
A B C N

A,B,C 각자 인원숨만큼 방에 넣을 수 있음, 총인원수 N명

빈침대 없이 방 배정 가능하면 1 불가능하면 0

5 9 12 113 -> 1

퓰이

A,B,C 다해서 최대 50 * 50 * 50 시간 2초 충분할 듯

'''


def check_avail(A,B,C,N):

    for i in range(300):
        for j in range(300):
            for k in range(300):
                if A*i + B*j + C*k == N:
                    return 1

    return 0

a,b,c,n = map(int,input().split())

print(check_avail(a,b,c,n))