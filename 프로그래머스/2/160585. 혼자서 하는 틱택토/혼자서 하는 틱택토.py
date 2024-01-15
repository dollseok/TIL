'''
3x3
선공 o 후공 x

실수 종류
1. o를 표시할 차례인데 x 를 표시하는 것 같이 반대로 할때도 잇다
2. 게임이 종료되어도 끝까지 진행

실수했는지 확인, 실수 없으면 계속 진행
계속 진행 가능이면 1, 아니면 0

선공이나 후공이 먼저 끝났는데 하나 더 놓았으면 0

풀이

X가 O보다 많을수 없다 -> X와 O의 개수 확인 -> O의 개수 >= X의 개수

dfs로 끝났는지 확인 -> stack
8방향
O가 끝났는지 확인 -> O의 개수 == X의 개수 +1
X가 끝났는지 확인 -> X의 개수 == O의 개수


'''
from collections import deque

direction = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

def solution(board):
    
    def check_bingo(x,y,index,target):
        dx,dy = direction[index]
        nx = x + dx
        ny = y + dy
        if 0<=nx<3 and 0<=ny<3 and board[nx][ny] == target:
            return True
    
    cnt_O = 0
    cnt_X = 0
    O_list = deque()
    X_list = deque()
    result = True
    
    # 개수 확인으로 한번 거름
    for i in range(3):
        for j in range(3):
            point = board[i][j]
            if point == 'O':
                O_list.append((i,j))
                cnt_O += 1
            elif point == 'X':
                X_list.append((i,j))
                cnt_X += 1
    
    # O의 개수 < X의 개수 -> 불가능
    if cnt_O < cnt_X:
        result = False
    # O의 개수 == X의 개수 -> O가 끝난게 있으면 안됨
    elif cnt_O == cnt_X:
        while O_list:
            x,y = O_list.popleft()
            for direction_index in range(8):
                dx,dy = direction[direction_index]
                nx = x + dx
                ny = y + dy
                if 0<=nx<3 and 0<=ny<3:
                    if board[nx][ny] == 'O':
                        if check_bingo(nx,ny,direction_index,'O'):
                            result = False
                            break
                
    # O의 개수 > X의 개수 -> X가 끝난게 있으면 안됨
    elif cnt_O == cnt_X + 1:
        while X_list:
            x,y = X_list.popleft()
            for direction_index in range(8):
                dx,dy = direction[direction_index]
                nx = x + dx
                ny = y + dy
                if 0<=nx<3 and 0<=ny<3:
                    if board[nx][ny] == 'X':
                        if check_bingo(nx,ny,direction_index,'X'):
                            result = False
                            break
                            
    else:
        result = False
        
    
    answer = -1
    if result:
        answer = 1
    else:
        answer = 0
    
    return answer