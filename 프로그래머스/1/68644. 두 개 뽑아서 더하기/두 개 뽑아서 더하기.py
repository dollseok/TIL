def solution(numbers):
    answer = set()
    
    l = len(numbers)
    for i in range(l - 1):
        for j in range(i+1, l):
            answer.add(numbers[i]+ numbers[j])
    
    answer = sorted(list(answer))
    return answer