# BAEKJOON class2 1085번 직사각형에서 탈출

'''
https://www.acmicpc.net/problem/1085

x,y : 시작점
w,h : 오른쪽 위 꼭짓점
0,0 : 왼쪽아래

각 거리를 리스트에 담아서 최솟값을 min으로 찾음
'''

import sys
sys.stdin = open('input.txt','r')

import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())    # 좌표를 받음

res = min([w-x, x, h-y, y])               # 최솟값의 결과

print(res)
