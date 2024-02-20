'''
11399번 ATM
'''

n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
result = 0

for i in range(1,len(arr)+1):
    result += i * arr[i-1]

print(result)