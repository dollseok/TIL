n = int(input())
data = list(map(int,input().split()))
M = max(data)

for i in range(len(data)):
    data[i] = (data[i]/M)*100

print(sum(data)/n)