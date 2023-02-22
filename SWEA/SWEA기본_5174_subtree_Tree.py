#SWEA 문제 해결 기본 5174번 subtree

'''
주어진 이진 트리에서 노드 N을 루트로 하는 서브트리에 속한 노드의 개수를 알아내는 프로그램
'''

import sys
sys.stdin = open("input.txt", "r")

def postorder_traverse(N):
    global cnt                     # 노드의 개수를 셀것
    cnt += 1
    if c1[N] != 0:                 # 이어진 노드가 첫번째에 있다면 (c1에 없으면 어차피 이어진 것이 없는것이라 여기만 선체크)
        LC = c1[N]                 # Left Child에 연결된 것도 확인
        postorder_traverse(LC)
        if c2[N] != 0:             # c1이 있었다면 c2도 확인
            RC = c2[N]             # Right Child에 연결된 것도 확인
            postorder_traverse(RC)

T = int(input())
for test_case in range(1,T+1):
    E,N = map(int, input().split())
    data = list(map(int, input().split()))
    cnt = 0                         # 서브트리의 노드의 개수
    # 트리제작    인덱스가 부모 노드
    c1 = [0]*(E+2)                  # 왼쪽 자식 노드, 정점 = E+1개, 인덱스 사용하려고 (E+1) +1
    c2 = [0]*(E+2)                  # 오른쪽 자식 노드, 정점 = E+1개, 인덱스 사용하려고 (E+1) +1
    for i in range(E):
        v1, v2 = data[2*i], data[2*i + 1]
        if c1[v1] == 0:             # c1이 비어있으면 c1에 추가
            c1[v1] = v2
        else:                       # c1이 이미 차있으면 c2에 추가
            c2[v1] = v2

    # 후위 순회로 개수 셀것             # 노드 N을 루트로 하는 트리의 노드 개수 세기
    postorder_traverse(N)

    print(f'#{test_case}', cnt)