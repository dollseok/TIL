'''



'''

def recur(depth,current):

    if depth == m:
        print(*ls)
        return

    for i in range(current,n+1):
        ls[depth] = i
        recur(depth + 1, i)


n,m = map(int,input().split())
ls = [0]*m

recur(0,1)