# BAEKJOON class2 1259번 팰린드롬 수

'''
https://www.acmicpc.net/problem/1259

뒤에서부터 읽어도 똑같으면 팰린드롬 수
'''

import sys
sys.stdin = open('input.txt','r')

while True:
    word = input()
    if word == '0':
        break

    elif word == word[::-1]:
        print('yes')

    elif word != word[::-1]:
        print('no')















