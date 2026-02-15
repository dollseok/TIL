'''
Docstring for 1068_g5

'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = list(map(int,input().split()))
delete = int(input())



children = [[] for _ in range(n)]
root = -1

for i in range(n):
    p = tree[i]
    if p == -1:
        root = i
    else:
        children[p].append(i)

def mark_deleted(x):
    deleted[x] = True
    for nxt in children[x]:
        if not deleted[nxt]:
            mark_deleted(nxt)

def count_leaves(x):
    if deleted[x]:
        return 0
    
    alive_children = [c for c in children[x] if not deleted[c]]
    if not alive_children:
        return 1
    
    return sum(count_leaves(c) for c in alive_children)


deleted = [False] * n

mark_deleted(delete)

if root == delete:
    print(0)
else:
    print(count_leaves(root))