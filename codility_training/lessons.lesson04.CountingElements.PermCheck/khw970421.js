//직접만든코드
function solution(A) {
    let count=0;
    A.sort((a,b)=>a-b);              //순서대로 분류
    A.reduce(function(accumulator,currentvalue){     //accumulator 0으로 설정 currentvalue A[0]으로 시작
        if(currentvalue-accumulator!=1)              // 둘의 차이가 1이 아니면 함수종료
            return -1;
        //둘의 차이가 1이면 count증가와 currentvalue값을 accumulator값으로 return
        count++;
        return currentvalue;

    },0)

    return (count==A.length)?1:0;                   //배열을 reduce에서 전부 순회하여 count와 A.length가 같으면 1 return 아니면 0 return
}

//피드백 받은코드1
function solution2(A) {
    return (A.sort((a,b)=>a-b).reduce(([acc, count], val) => {     //accumulator 0으로 설정 currentvalue A[0]으로 시작
        if(val - acc !== 1)              // 둘의 차이가 1이 아니면 함수종료  console.log([1]-[1]==0); 결과 true
            return [-1,0];
        //둘의 차이가 1이면 count증가와 currentvalue값을 accumulator값으로 return
        count++;
        return [val,count];
    }, [ 0, 0 ])[1] === A.length); //배열을 reduce에서 전부 순회하여 count와 A.length가 같으면 1 return 아니면 0 return
}

//피드백 받은코드2
function solution3(A){
    return !(A.sort((a, b) => a - b).find(function(v, k){
        console.log(v,k);
        return (v - 1 !== k);}          //1부터 나열했을때 값 - 1 이 index값이랑 같지않은값(순열이 아닐때)이 있으면 return에 false를 만든다
    ));
}

//true false를 1,0으로 변환하려면 *1을한다. true * 1 = 1 , false * 1 = 0

console.log(solution3([4, 1, 3, 2])==1);
console.log(solution([4, 1, 3])==0);
console.log(solution2([4, 1, 3])==0);
console.log(solution3([4, 1, 3])==0);
