function solution(arr, divisor) {
    let answer=[];
    arr.forEach(function(e){
        if(e%divisor==0)        //나누어 떨어지면 추가
            answer.push(e);
    })
    answer.sort((a,b)=>a-b);        //정렬
    return (answer.length>0)?answer:[-1];       //값이 존재하면 answer 아니면 [-1]리턴
}
