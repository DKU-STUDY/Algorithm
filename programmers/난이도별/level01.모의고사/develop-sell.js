function solution(answers) {
    let answer = [1,2,3]
    const p1 = [1,2,3,4,5] //5
    const p2 = [2,1,2,3,2,4,2,5] //8
    const p3 = [3,3,1,1,2,2,4,4,5,5]    //10
   
    let p1_c = answers.filter((v, i) => (p1[i % 5] === v ? v : "")).length
    let p2_c = answers.filter((v, i) => (p2[i % 8] === v ? v : "")).length
    let p3_c = answers.filter((v, i) => (p3[i % 10] === v ? v : "")).length
    
    let arr = [p1_c, p2_c, p3_c];
    let max = 0; 
    max = p1_c > p2_c ? p1_c : p2_c;
    max = max > p3_c ? max : p3_c
    
    
    return answer.filter((v, i) => (arr[i] >= max ? v : ""));
}

// 문제풀이: 
// player 1,2,3의 답이 계속 중복되는데, 
// 이때 중복되는 구간의 사이즈가 다르다. 1부터 5,8,10 사이즈 
// 그래서 먼저 그 구간을 값을 넣은 배열로 const 지정해줬다.
// 그 후 filter 함수를 통해 answers 배열과 맞는 경우만 탐색해서 그것의 length를 구해서
// 맞은 갯수가 알게 되었다. 
// 이때 p2[i % 8] 이런식으로 하면 딱 안 나눠지는 부분까지 캐치하게 된다 (중요 포인트!)

// 그 후 값들의 가장 큰 값을 max 구해서, max과 같거나 큰 answer를 filter해서 제출한다. 

// 배운점: 
// Math.max 함수 존재
// var max = Math.max(a1c,a2c,a3c);
