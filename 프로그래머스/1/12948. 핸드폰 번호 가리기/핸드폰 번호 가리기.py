def solution(phone_number):
    
    slice_data = phone_number[-4:]
    star_count = (len(phone_number) - 4) 
    
    answer = star_count * '*' + slice_data
    
    
    return answer