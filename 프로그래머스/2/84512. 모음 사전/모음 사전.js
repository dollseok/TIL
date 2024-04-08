/*
A -> AA -> .... -> UUUUU(마지막)
['', A , E , I , O , U] 6*6개의 경우의 수

A AA AAA AAAA AAAAA AAAAE AAAAI AAAAO AAAAU AAAEA AAAEE
*/



function solution(word) {
    const DATA = ['A', 'E', 'I', 'O', 'U']
    let flag = false
    let cnt = 0
    
    function check(string,target){
        cnt ++
        if (string === target) {
            return true
        }
    }
    
    for (a=0;a<5;a++){
        let firstStr = DATA[a]
        if (check(firstStr,word)) {return cnt}
        for(b=0;b<5;b++){
            let secondStr = DATA[a]+DATA[b]
            if (check(secondStr,word)) {return cnt}
            for(c=0;c<5;c++){
                let thirdStr = DATA[a]+DATA[b]+DATA[c]
                if (check(thirdStr,word)) {return cnt}     
                for(d=0;d<5;d++){
                    let fourthStr = DATA[a]+DATA[b]+DATA[c]+DATA[d]
                    if (check(fourthStr,word)) {return cnt}
                    for(e=0;e<5;e++){
                        let fourthStr = DATA[a]+DATA[b]+DATA[c]+DATA[d]+DATA[e]
                        if (check(fourthStr,word)) {return cnt}
                    }
                } 
            }
        }
    }

}