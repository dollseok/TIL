def dfs(n,computers,com,visited):
    visited[com] = True
    for i in range(n):
        if i != com and computers[i][com] == 1 and not visited[i]:
            dfs(n,computers,i,visited)

def solution(n, computers):
    answer = 0

    visited = [False] * n
    
    for com in range(n):
        if not visited[com]:
            dfs(n,computers,com,visited)
            answer += 1
    
    return answer