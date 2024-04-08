'''
주어지는 queries => 왼쪽 끝 오른쪽 끝
ex)
2,2,5,4
2,2  ->  2,4  ->  5,4  ->  5,2  ->  2,2
   (0,1)  (1,0)      (0,-1)   (-1,0)
'''


def solution(rows, columns, queries):
    dr = [0,1,0,-1]
    dc = [1,0,-1,0]
    
    answer = []
    
    arr = [[j*columns + (i + 1) for i in range(columns)] for j in range(rows)]
    
    for query in queries:
        start_row = query[0]-1
        start_col = query[1]-1
        
        end_row = query[2]-1
        end_col = query[3]-1
        
        r = start_row
        c = start_col
        
        direction_idx = 0
        current_num = arr[r][c]
        
        min_num = 1e9
        while True:
            nr = r + dr[direction_idx]
            nc = c + dc[direction_idx]
            
            if not start_row <= nr <= end_row or not start_col <= nc <= end_col:
                if direction_idx == 3:
                    break
                
                direction_idx += 1
                continue
            
            next_num = arr[nr][nc]
            arr[nr][nc] = current_num
            current_num = next_num
            r,c = nr,nc
    
            min_num = min(min_num,current_num)
        
        answer.append(min_num)
    
    return answer