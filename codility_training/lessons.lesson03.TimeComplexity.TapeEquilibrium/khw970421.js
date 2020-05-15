function solution(A) {
   let sum=0;
   const size = A.length,last = A.length+1 ;//길이저장
    let all=0,min=Infinity,final;             //배열의 총합저장 하는 all, P에따른 difference값인 final
    for(let k=0;k<size;k++)                 //배열 총합구하기
        all+=A[k];

    for(let i=0;i<size-1;i++)
    {
        sum+=A[i];                          //앞에 있는 P=i+1일때의 앞의값 구하기
        final = Math.abs(all - sum * 2)                  //final은 뒤의값-앞의값의 절대값 | (all-sum)-sum | ,음수면 절대값을 붙인다.
        min=Math.min(min,final);            // 작은 값을 min에 넣기
     }
    let k =[0, 1, 2, 3, 4].reduce( (pre, curr) => pre + curr );
    console.log(k);
   return min;                              //P를 만족하는 가장 작은 min return
}

console.log(
    solution([3, 1, 2, 4, 3]) === 1,
    solution([-1000, 1000]) === 2000,
    solution([1, 2]) === 1
);


