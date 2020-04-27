  
function solution(N) {
    let a=[];               //배열생성
    let max_result=0;
    
     for(let i=0;N>=1;i++)
     {
        a[i]=N%2;
        N=(N-N%2)/2;                  //a배열에 0과1의 이진수 값들 각각 넣기
     }
     const a_length = a.length;
     for(let j=0;j<a_length;j++)     //a배열 크기만큼 반복
     {
         let sum=0,p=1;             //sum 과 p는 j가 바뀔때마다 새로 설정
         
         if(a[j]==1)                //어떤 a[j]가 1이라면
         {
             do{
                 if(a[j+p]==0)      //그 후 차례로 0이 계속나올때까지 반복하며 sum을 증가시킨다.
                 {
                     p++;
                     sum++;
                 }
             }
             while(a[j+p]==0)
         }
         
         if(max_result<sum) max_result=sum;            //가장 큰 gap 차이 max_result에 넣기
         
     }
    return max_result;
}
