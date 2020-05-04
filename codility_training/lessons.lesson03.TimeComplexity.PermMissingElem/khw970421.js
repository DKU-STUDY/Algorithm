function solution(A) {
   let sum1=0,sum2=0,size=A.length;
   let i;
   
       sum1=size*(size+1)/2;             //1부터 N까지 더한다.
       sum2=A.reduce((a,b)=>a+b);              //배열 범위에 존재하는 값들을 전부 더한다.
   
   sum1+=(size+1);                 //N+1도 존재하는것도 더해 전체 1~N+1까지의 총합을 구한다.
   return sum1-sum2;            //전체 1~N+1중에서 빠진 하나의 값을 제외한 총합을 빼서 빠진 값을 구한다.
}
