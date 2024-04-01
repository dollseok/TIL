/*
소수 구하기 -> 에라토스테네스의 체
진수 바꾸기


*/
function eratos(number){
    if (number <= 1) return false
    
    for (i=2; i<=Math.sqrt(number); i++) {
        if (number%i === 0){
            return false
        }
    }
    return true
}


function solution(n, k) {
    var answer = -1;
    let answer_list = []
    let num_list = []
    // num_list 만들기
    while (n > 0){
        num_list.unshift(n%k)
        n = Math.floor(n/k)
    }
    let str = ''
    num_list.forEach(number => {
        if(number === 0){
            if (str !== ''){
                answer_list.push(str)    
            }
            str = ''
        } else {
            str += number
        }
    })
    if (str !== ''){
        answer_list.push(str) // 마지막 str 추가    
    }

    // 소수인지 판별
    let result = 0
    answer_list.forEach(number=>{
        if (eratos(Number(number))){
            result += 1
        }
        
    })
    
  
    answer = result
    
    
    return answer;
}