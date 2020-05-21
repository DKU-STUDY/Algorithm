function solution(A) {
    let count=0;
    A.sort((a,b)=>a-b);              //순서대로 분류
    A.reduce(function(accumulator,currentvalue){     //accumulator 0으로 설정 currentvalue A[0]으로 시작
        if(currentvalue-accumulator!=1)              // 둘의 차이가 1이 아니면 함수종료
            return -1;
        else{                                        //둘의 차이가 1이면 count증가와 currentvalue값을 accumulator값으로 return
            count++;
            return currentvalue;
        }
    },0)

    return (count==A.length)?1:0;                   //배열을 reduce에서 전부 순회하여 count와 A.length가 같으면 1 return 아니면 0 return
}

console.log(solution([4, 1, 3, 2])==1);
console.log(solution([4, 1, 3])==0);