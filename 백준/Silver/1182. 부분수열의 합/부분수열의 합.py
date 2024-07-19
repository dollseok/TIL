def dfs(lst,idx):
    global cnt
    if idx == n:
        return

    lst.append(arr[idx]) # 리스트에 먼저 더해서 확인 해보고 다음으로

    if sum(lst) == s and lst != []:
        cnt += 1

    dfs(lst,idx+1)
    lst.pop()
    dfs(lst,idx+1)

n,s = map(int,input().split())
arr = list(map(int,input().split()))

cnt = 0
dfs([],0)

print(cnt)