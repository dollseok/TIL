/*
연속하는 수의 합이 맞아야 함

두포인터로 풀어야할 것 같음
left,right
원하는 수의 합 k
현재 값 sum
sum < k 면 right + 1
sum > k 면 left == right면 left+= 1 right += 1 / left + 1
sum = k 면 길이 비교해서 짧은걸로
*/



function solution(sequence, k) {
    const LENGTH = sequence.length-1
    var answer = [0,LENGTH];
    let left = 0
    let right = 0
    let sum = sequence[0]
    
    function leftmove(){
        sum -= sequence[left]
        left ++
        if (left > right){
            right ++
            sum += sequence[right]
        }
    }
    
    function rightmove(){
        if (right < LENGTH) {
            right ++
            sum += sequence[right]
        }
        else {
            sum -= sequence[left]
            left ++
        }
    }
    
    while (left <= LENGTH){
        if (sum < k){
            rightmove()
        } else if(sum > k){
            leftmove()
        } else {
            if (answer[1]-answer[0] > right-left){
                answer = [left,right]
            }
            leftmove()
        }
    }
    
    
    return answer;
}