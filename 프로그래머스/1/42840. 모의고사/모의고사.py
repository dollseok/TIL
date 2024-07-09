def solution(answers):
    pick_lst =[[1,2,3,4,5],[2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    count = [0,0,0]
    idx = 0
    
    for lst in pick_lst: 
        answer_idx = 0
        len_answer = len(answers)   
        lst_idx = 0
        len_lst = len(lst)

        for i in range(len_answer):
            if answers[answer_idx] == lst[lst_idx]:
                count[idx] += 1
                
            answer_idx = answer_idx + 1
            lst_idx = (lst_idx + 1) % len_lst
        
        idx += 1
    
    result_lst = []
    for i in range(len(count)):
        if count[i] == max(count):
            result_lst.append(i+1)
            
    answer = result_lst
    return answer