# 백준 4153번 직각삼각형

'''
직각 삼각형인지 확인
'''

# import sys
# sys.stdin = open('input.txt', 'r')

while True:
    a, b, c = map(int,input().split())
    if a == 0 and b == 0 and c == 0:
        break
    elif a**2 + b**2 == c**2 or a**2 == b**2 + c**2 or a**2 + c**2 == b**2 :
        print('right')
    else:
        print('wrong')
