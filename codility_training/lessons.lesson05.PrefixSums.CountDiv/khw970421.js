//처음 시도한 성공결과 => 성능에서 50점
function solution(A, B, K) {
    const k=[];
    let p=0;
    for(let i=A;i<=B;i++){
        k[p]=i;
        p++;
    }
    let count;
    count=k.filter(element=>element%K==0);
    return count.length;
}

//성능을 높이기 위해 한 최종코드
function solution1(A, B, K) {
    return Math.floor(B/K)-Math.ceil(A/K)+1; //A랑B가 나눠떨어지면 나눈 크기들의 차+1로 갯수를 구하고
    //A가 안나눠지면 A가 갯수에 포함이 안되게 ceil로 올려주고
    //B가 안나눠지면 B가 갯수에 포함이 안되게 floor해준다.
}

console.log(solution1(6,10,2)==3);
console.log(solution1(7,10,2)==2);
console.log(solution1(5,10,3)==2);
