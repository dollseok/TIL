# Baekjoon 2527번 직사각형


# import sys
# sys.stdin = open('input.txt', 'r')

for i in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = list(map(int,input().split()))

    # 완전 외부인 경우 d
    if (p2 < x1) or (p1 < x2) or (y1 > q2) or (y2 > q1):
        print('d')

    # 점으로 겹치는경우 c
    elif x1 == p2 and y1 == q2:
        print('c')
    elif x2 == p1 and q1 == y2:
        print('c')
    elif p2 == x1 and y2 == q1:
        print('c')
    elif p1 == x2 and y1 == q2:
        print('c')

    # 선이 겹치는 경우 b
    elif x1 == p2 or x2 == p1:
        if (y1 <= y2 <= q1) or (y1 <= q2 <= q1) or (q2 >= q1 and y2 <= y1) :
            print('b')

    elif y1 == q2 or q1 == y2:
        if (x1 <= x2 <= p1) or (x1 <= p2 <= p1) or (p2 >= p1 and x2 <= x1):
            print('b')
    # 나머지 a
    else:
        print('a')
