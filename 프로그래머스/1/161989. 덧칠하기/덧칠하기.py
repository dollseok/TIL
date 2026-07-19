def solution(n, m, section):
    wall = [1] * n
    count = 0
    for i in section:
        wall[i - 1] = 0
    
    idx = 0
    while idx < n:    
        if wall[idx] == 1:
            idx += 1

        else:
            max_range = min(n, idx + m)
            count += 1
            for i in range(idx, max_range):
                wall[i] = 1
            idx += m
    
    return count