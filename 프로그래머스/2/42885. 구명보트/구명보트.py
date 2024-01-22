'''
limit은 구명 보트의 무게 제한, 최대 2명
보트의 최솟값
people 1 - 50000명
몸무게 , 제한 40 - 240
최대한 한계까지 맞춰야함
'''

def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    result = 0
    
    while left < right:
        sum = people[left] + people[right]
        if sum > limit:
            result += 1
            right -= 1
        else:
            result += 1
            right -= 1
            left += 1      
            
    if left == right:
        result += 1
    
    answer = result
    return answer