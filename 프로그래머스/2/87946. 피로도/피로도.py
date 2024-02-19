'''
던전개수는 1-8 -> dfs로도 충분할듯
순서를 어떻게?

'''

visited = [False]*9
result = 0

def dfs(current_energy, dungeons, cnt):
    global result, visited
    
    if  cnt == len(dungeons):
        result = cnt
        return
    
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= current_energy and dungeons[i][1] <= current_energy:
            visited[i] = True
            dfs(current_energy-dungeons[i][1], dungeons, cnt + 1)
            visited[i] = False
            
    result = max(result,cnt)

def solution(k, dungeons):
    global result, visited
    dfs(k,dungeons, 0)
    answer = result
    return answer