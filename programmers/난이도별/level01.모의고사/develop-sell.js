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