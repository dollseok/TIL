#SWEA 1979번 D2 어디에 단어가 들어갈 수 잇을까?
'''
문제 링크
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYXI5IoKVCoDFAQK&contestProbId=AV5PuPq6AaQDFAUq&probBoxId=AYXI6OVKVLQDFAQK&type=PROBLEM&problemBoxTitle=D2&problemBoxCnt=5


'''


T = int(input())

for test_case in range(1,T+1):

    n,k = map(int,input().split())

    board = [input().split() for _ in range(n)]  # 한줄 한줄 가져온 것, 2차원 입력값 list에 저장하기 n x n

    # input().split()을 n회만큼 한것
    # [
    # [0, 0, 1, 1, 1]
    # [1, 1, 1, 1, 0]
    # [0, 0, 1, 0, 0]
    # [0, 1, 1, 1, 1]
    # [1, 1, 1, 0, 1]
    # ]
    # print(board) #리스트 안의 리스트가 된다.

    word = '1'*k

    #가로
    cnt = 0
    for i in range(n) :
        row = ''.join(board[i]) # 하나로 일단 합쳐준다
        row_1 = row.split('0')  #0을 기준으로 분리 시킨다.
        cnt += row_1.count(word)  # 111이 리스트 안에 있으면 개수를 센다

    #세로

    for c in range(n):

        column_list_i = []
        for i in range(n):
            column_list_i.append(board[i][c])

        col = ''.join(column_list_i)
        col_1 = col.split('0')
        cnt += col_1.count(word)

    print(f'#{test_case} {cnt}')



# 줄인 풀이

T = int(input())

for test_case in range(1,T+1):

    n,k = map(int,input().split())
    board = [input().split() for _ in range(n)] 
    word = '1'*k
    cnt = 0

    #가로   
    for i in range(n) :
        row = ''.join(board[i]) # 하나로 일단 합쳐준다
        cnt += (row.split('0')).count(word)  # 0을 기준으로 분리시키고 111이 리스트 안에 있으면 개수를 센다

    #세로
        column_list_i = ''.join([board[j][i] for j in range(n)]) #일정한 i에 대해 j를 추출해 column 을 만든다
        cnt += (column_list_i.split('0')).count(word)

    print(f'#{test_case} {cnt}')




# 성민님 풀이

t=int(input())
 
for z in range(1,t+1):
 
      a,b=map(int,input().split())
 
      lst=[input().split() for i in range(a)]
      print(lst)
      total=0
      for i in range(a):
 
            c=list((''.join(lst[i])).split('0'))
            print(c)
            c2 = list((''.join([lst[j][i] for j in range(a)])).split('0'))
             
            total += (c.count('1'*b) + c2.count('1'*b))
      print(f'#{z} {total}')






