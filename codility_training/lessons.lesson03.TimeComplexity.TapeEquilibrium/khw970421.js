function solution(A) {
   let size=A.length,sum=0;//길이저장
    let all=0,result,min=100000;
    for(let k=0;k<size;k++)
        all+=A[k];

    for(let i=1;i<size;i++)
    {

        sum+=A[i];
        result = all-sum*2;
        if(result<0)    result*=-1;
        console.log(result);
        min=Math.min(min,result);


   }

   return min;

}

console.log(
    solution([3, 1, 2, 4, 3]) === 1,
    solution([-1000, 1000]) === 2000,
    solution([1, 2]) === 1
);


