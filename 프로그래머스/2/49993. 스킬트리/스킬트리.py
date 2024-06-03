'''
skill 길이 1~26
skill-trees : 1-20개
각 원소 2~26 문자열

''' 

def solution(skill, skill_trees):
    
    answer = -1
    cnt = 0
    
    
    for skill_tree in skill_trees:
        visited = [False] * len(skill)

        flag = False
        
        for skill_pick in skill_tree:

            if skill_pick in skill:
                idx = skill.index(skill_pick)
    
                visited[idx] = True

                for check in range(idx):
                    if not visited[check]:
                        flag = True
                        break
            if flag:
                break
            
        if not flag:
            cnt += 1 
        
        
        answer = cnt
            
    return answer