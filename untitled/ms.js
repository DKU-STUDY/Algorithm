function solution(N) {
    let k=N.toString(2);                        //문자열 2진수로 설정
    let count=0,max=0;                          //0을세는 count, 0이연속인 최대크기 max
    let h = [...k];                             //문자열을 배열로 변경
    let reducer = function(accumulator,value)   // h.reduce함수에 initialvalue가 없으므로 accumulator에 배열의 첫번째값, value에 배열의 두번째값 입력
    {
        if(value==0)                            //배열값이 0이라면 count 증가
                count++;
        else {
            max = Math.max(max, count);         //배열값이 1이되면 그때 최대치인 max와 비교하기 (1000이면 count를 세어도 max와 비교하지않는다.)
            count = 0;                          //count를 0으로 초기화
        }
    }
    h.reduce(reducer);                          //reduce함수 사용
    return max;
}

console.log(solution(1041)===5);
console.log(solution(15)===0);
console.log(solution(32)===0);
