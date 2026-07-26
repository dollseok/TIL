def solution(N, stages):
    answer = []
    people = len(stages)
    
    for stage in range(1,N+1):
        failed = stages.count(stage)
        if people == 0:
            failure_rate = 0
        else:
            failure_rate = failed / people
        
        answer.append((stage,failure_rate))
        
        people -= failed
    
    answer.sort(key=lambda x: (-x[1],x[0]))
    
    return [stage for stage, rate in answer]