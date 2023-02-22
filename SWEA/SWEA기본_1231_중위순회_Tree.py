#SWEA 문제해결 기본 1231번 중위순회

'''
1-N까지의 자연수를 이진탐색 트리에 저장
이진탐색 트리의 특성을 이용해서 풀어보기
2**n 으로 커지는 개수 특성


'''

# 내가 푼 풀이

import sys
sys.stdin = open("input.txt", "r")

def inorder(node):
    global res
    if node != 0:
        inorder(int(tree[node][2]))
        res.append((tree[node][1]))
        inorder(int(tree[node][3]))

for test_case in range(1,11):
    N = int(input())
    tree = [0]                  # 인덱스를 이용할 것이라서 0을 미리 추가
    res = []                    #

    for i in range(N):
        data = list(input().split())
        if len(data) == 4:
            tree.append(data)
        elif len(data) == 3:
            tree.append(data + [0])
        elif len(data) == 2:
            tree.append(data + [0,0])

    # print(tree)

    inorder(1)
    print(f'#{test_case}', ''.join(res))
