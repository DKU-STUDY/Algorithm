function solution(A) {
   let size=A.length;                       //길이저장
   let sum=0,min=100000,first_size;            //first_size는 P=1일때 sum은 P에 대해 반복 min은 많이 큰 수 
   for(let i=1;i<size;i++)
   {    
        sum+=A[i];
        if(sum<0)sum*=-1;
   }                                 
   first_size=sum-=A[0];             //P=1일때 sum의 값을 구한다.
   //ddddd
   for(let p=1;p<size;p++) {
       sum -= A[p] * 2;              //P의 다음값은 원래 있던 A[P-1]*2만큼 차이 나기때문에 계산
       if (sum < 0) sum *= -1;        // 음수일경우 절대값을 씌운다.
       min = Math.min(min, sum);   // 이를 만족하는 가장 작은 min을 찾는다.

   }
   min=Math.min(min,first_size);    //처음 P=1일때와는 비교하지 못했으므로 마지막으로 비교
   return min;

}

console.log(
    solution([3, 1, 2, 4, 3]) === 1,
    solution([-1000, 1000]) === 2000,
    solution([1, 2]) === 1,
    solution()

);


