'''
dr 2가지 방향
[x,y] x + 1하는 방향
[x,y] y + 1하는 방향
[x,y] x,y 둘다 -1 하는 방향
'''



def solution(n):
    dx = [1,0,-1]
    dy = [0,1,-1]
    dr = 0
    
    arr = [[0]*i for i in range(1,n+1)]
    x,y = [0,0] # start point
    arr[x][y] = 1
    
    while True:
        tx = x + dx[dr]
        ty = y + dy[dr]
        if 0 <= tx < n and 0<= ty <= tx and arr[tx][ty] == 0: # 삼각형 내에 있으면
            arr[tx][ty] = arr[x][y] + 1 
            x = tx
            y = ty
        else:       
            cnt = 0
            for i in range(dr, dr+3):
                i = i % 3
                if 0 <= x+dx[i] <n and 0 <= y+dy[i] <= x+dx[i]:
                    if arr[x+dx[i]][y+dy[i]] != 0:
                        cnt += 1
                else:
                    cnt += 1
                
            if cnt == 3:
                break
                
            dr = (dr + 1) % 3
            
    result = []
    for arritem in arr:
        for i in arritem:
            result.append(i)
            
    answer = result
    return answer