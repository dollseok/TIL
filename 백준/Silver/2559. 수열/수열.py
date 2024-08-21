'''
수열

연속적인 며칠동안 온도합이 가장 큰값

연속적인 K 개의 합
prefix 를 구하고 N

prefix를 구간별로 한번 더 돌려서 k 구간 값을 구함 N

=> 2N정도의 시간 복잡도를 가질 것

반례

-> 앞에 0인 부분이 최대값이 되는 경우를 제외해야한다.
-> 리스트를 애초에 작게 만들던가, 아니면 K ->N 까지 리스트를 순회하며 최대값을 뽑는게 안정적
'''

N,K = map(int,input().split())

ls = [0] + list(map(int,input().split()))

prefix_sum = [0] * (N+1)
prefix_k_sum = [0] * (N+1-K)

for i in range(1,N+1):
    prefix_sum[i] = prefix_sum[i-1] + ls[i]

# 1번 방안
for i in range(K,N+1):
    prefix_k_sum[i-K] = prefix_sum[i] - prefix_sum[i-K]

print(max(prefix_k_sum))

# 2번 방안
# result = -100 * 100000
# for i in range(K,N+1):
#     result = max(result,prefix_sum[i] - prefix_sum[i-K])
# print(result)


