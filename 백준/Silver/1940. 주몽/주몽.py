
N = int(input())
M = int(input())
gradient = list(map(int,input().split()))

gradient.sort()

min_gradient = 0
max_gradient = N - 1

r = 0
while True:
    
    if max_gradient == min_gradient:
        break

    if gradient[max_gradient] + gradient[min_gradient] > M:
        max_gradient -= 1
    elif gradient[max_gradient] + gradient[min_gradient] < M:
        min_gradient += 1
    else:
        max_gradient -= 1
        r += 1


print(r)      
        
    
    