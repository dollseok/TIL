def solution(nums):
    answer = 0
    
    m = max(nums) * 3
    prime = [True] * (m + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(m ** 0.5) +  1):
        if prime[i]:
            for j in range(i*i, m + 1,i):
                prime[j] = False
    
    l = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                l.append(nums[i]+ nums[j] + nums[k])
    
    for num in l:
        if prime[num]:
            answer += 1
        
    
    return answer