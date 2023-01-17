# SWEA

## D1

### 2070번. 큰 놈, 작은 놈, 같은 놈
--- 
- 아직 첫번째 input 숫자 하나로 받는 것 그리고 뒤에 연속으로 나오는 input을 map과 split으로 받는 것 기억하기

```python

#input
'''
3
3 8 
7 7 
369 123      

'''

T = int(input()) 
    #첫번째 input을 받음
for test_case in range(1, T + 1): 
    # 받은 input으로 range 설정
    a,b = map(int,input().split()) 
    # 후에 각 input을 나누어서 받음
   
    if a > b:
        print(f'#{test_case} >')
    elif a < b:
        print(f'#{test_case} <')
    else :
        print(f'#{test_case} =')


'''        
#1 <
#2 =
#3 >
'''

```

