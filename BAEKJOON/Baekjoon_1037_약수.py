#백준 1037번 약수

'''
https://www.acmicpc.net/problem/1037

양수 A가 N의 진짜 약수가 되려면 N은 A의 배수 , A != 1&N 이어야 한다.

풀이 : 나는 최대 최소값을 곱하면 A가 나올 것이라 생각했다.
'''

import sys
sys.stdin = open("input.txt", "r")

N = int(input())
measure_list = list(map(int,input().split()))
print(min(measure_list) * max(measure_list))

