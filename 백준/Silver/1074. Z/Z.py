n,r,c = map(int,input().split())

arr_size = 2**n

# 몇 분면에 위치해있는지가 제일 중요하다
'''
arr_size의 절반을 기준으로 r,c위치 확인
arr_size//2 r , c
'''
sp = 0

while arr_size != 1:
    arr_size = arr_size//2
    if r < arr_size and c < arr_size:
        sp += 0
    elif r < arr_size and c >= arr_size:
        # 2분면
        sp += (arr_size ** 2) * 1
        c -= arr_size
    elif r >= arr_size and c < arr_size:
        # 3분면
        sp += (arr_size ** 2) * 2
        r -= arr_size
    else:
        # 4분면
        sp += (arr_size ** 2) * 3
        r -= arr_size
        c -= arr_size

print(sp)