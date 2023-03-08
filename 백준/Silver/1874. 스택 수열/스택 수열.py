# 백준 1874번 스택 수열

'''
스택
나중에 들어간 자료가 먼저 나옴

1-n 수르 스택에 넣었다가 뽑아 늘어놓음으로 하나의 수열을 만듦

스택에 push 하는 순서는 오름차순
가장 큰것이 들어가면 pop

'''

# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
stack = []

sort_stack = [i for i in range(N, 0 , -1)]
# print(sort_stack)    # 1 - n까지 확인하는데 pop으로 뽑아오는게 빨라서 역순으로 리스트에 저장

lst = [int(input()) for _ in range(N)]
# print(lst)           # 완성되어야할 리스트
i = 0
res = []               # + push, - pop 결과를 넣을 리스트
check_lst = []         # 결과를 넣어 체크할 리스트

while i != N:          # 체크리스트 끝까지 확인할 때까지 반복
    if sort_stack:                              # sort_stack이 남아있으면
        stack.append(sort_stack.pop())          # sort_stack에서 pop해서 stack에 추가
        res.append('+')                         # res에 + 추가
        
    if stack and stack[-1] == lst[i]:           # stack이 있고, stack 마지막 값과 lst i번째가 같으면 
        while stack[-1] == lst[i]:              # stack 마지막 값과 lst i번째가 같을 동안 반복 , 달라지면 끝    
            check_lst.append(stack.pop())       # check_lst에 stack에서 pop한 숫자를 넣어줌 
            i += 1                              # 다음 i 확인
            res.append('-')                     # pop을 해서 '-' 추가
            if i == N or not stack:             # i ==N 까지 봤거나 stack이 비었을 때 break 
                break

    elif not stack or not sort_stack:           # 스택이나 sort stack이 비었을 때 break
        break

if check_lst == lst:
    for i in res:
        print(i)
else:
    print('NO')



