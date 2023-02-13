#백준 1059번 좋은 구간

'''
https://www.acmicpc.net/problem/1059

`
'''



import sys
sys.stdin = open("input.txt", "r")

L = int(input())                         # 집합의 크기
nums = list(map(int, input().split()))   # 집합 숫자 리스트
n = int(input())                         # 판단할 n의 값
nums.append(n)
nums.sort()                         # 정렬해서 n의 위치가 어디의 중간인지 알아야한다.
i = nums.index(n)

if len(set(nums)) == L:             # 만약 nums에 잇는 숫자라면 n이 들어와도 set으로 중복 없애면 그대로 일 것
    total_count = 0                 # 겹치면 부분집합 없음 = 0

elif n <= min(nums):                # n 범위가 1~50이므로 가장 작은 수보다 작을 수 있다. n이 집합의 최소값일 때
    r_count = (nums[i + 1] - 1) - nums[i]     # n을 기준으로 오른쪽
    l_count = nums[i] - 1                     # n을 기준으로 1부터
    total_count = r_count + l_count + r_count * l_count

else:                               # 일반적인 경우일 때
    r_count = (nums[i+1] - 1) - nums[i]       # n을 기준으로 오른쪽
    l_count = nums[i] - (nums[i-1] + 1)       # n을 기준으로 왼쪽
    total_count = r_count + l_count + r_count * l_count

print(total_count)

# n 기준
# 오른쪽 개수 = ((nums[i+1] - 1) - n)
# 왼쪽 개수 = (n - (nums[i-1] + 1))
# 전체 개수 = 오른쪽 개수 * 왼쪽 개수 + 오른쪽 개수 + 왼쪽 개수