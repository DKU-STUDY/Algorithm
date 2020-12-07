 function solution(participant, completion) {
    let answer = '';
    participant.sort();
    completion.sort();
    const len = participant.length
    for(let j = 0; j < len; j ++){
        for(let i = 0; i < completion.length; i++){
            if (participant[j] === completion[i]){
                completion.splice(i, 1)
                participant.splice(j, 1)
                j--;
                break;
            }
        }  
    }
    //participant.map((word, index) => word + index);
    //console.log(participant.filter((word) => completion.indexOf(word) < 0));
    return participant[0];
}

//처음 해법 => 효율성에서 문제

function solution(participant, completion) {
    let answer = '';
    participant.sort();
    completion.sort();
    const len = participant.length;
    let i = 0;
    while(i < len) {
        if (participant[i] !== completion[i])
            return participant[i];
        i++;
    }    
}

// 문제 풀이: 
// 효율성 문제 때문에 최대한 이중 for문을 안 사용하려고 고민을 많이 했다. 
// 그러나 해결하기 어려워서, 우선 sort함수로 순서를 맞춰주면 비교적
// 괜찮을 것 같아보였다. 
// 그래도 해결이 안되어서 length 함수를 계속 호출하지 않도록 밖으로 뺐다.
// 그래도 해결이 안되어서 고민하다 

// eyabc.js 님의 풀이를 참고했다. 
// sort를 하면 순서대로 짜지기 때문에 달라지는 순번의 요소가 정답이었다. 
// participant와 completion의 길이 차이가 -1이기 때문. 

// 배운 점: 
// for문을 줄이는 연습을 더 해보자..! 