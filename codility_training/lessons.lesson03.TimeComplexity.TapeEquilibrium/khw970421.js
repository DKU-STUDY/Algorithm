function solution(A) {
   let size=A.length,sum=0;//길이저장
    let all=0,min=100000,final;             //배열의 총합저장 하는 all, P에따른 difference값인 final
    for(let k=0;k<size;k++)                 //배열 총합구하기
        all+=A[k];

    for(let i=0;i<size-1;i++)
    {
        sum+=A[i];                          //앞에 있는 P=i+1일때의 앞의값 구하기
        final = all-sum*2;                  //final은 앞의값 (all-sum)-sum
        if(final<0)    final*=-1;           //음수면 절대값을 붙인다.
        min=Math.min(min,final);            // 작은 값을 min에 넣기
     }
   return min;                              //P를 만족하는 가장 작은 min return
}

console.log(
    solution([3, 1, 2, 4, 3]) === 1,
    solution([-1000, 1000]) === 2000,
    solution([1, 2]) === 1
);


