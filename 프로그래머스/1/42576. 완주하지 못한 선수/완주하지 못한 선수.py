def solution(participant, completion):
    runners = {}
    
    for i in participant:
        runners[i] = runners.get(i,0) + 1
    
    for name in completion:
        runners[name] -= 1
    
    for name, count in runners.items():
        if count > 0:
            return name
