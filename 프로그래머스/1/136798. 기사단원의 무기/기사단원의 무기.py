def count_divisor(num):
    count = 0
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            count += 2
            if i*i == num:
                count -= 1
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        divisor_count = count_divisor(i)
        
        if divisor_count >  limit:
            answer += power
        else:
            answer += divisor_count

    return answer