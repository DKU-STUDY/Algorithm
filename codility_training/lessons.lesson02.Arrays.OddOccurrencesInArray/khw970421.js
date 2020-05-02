// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    let size = A.length;                //A의 크기 저장
    for(let i=0;i<size;i++)             //크기만큼 반복
    {       
        if(A[i]==0) continue;           //A[i]가 0이면 j의 for문을 반복하지않는다.(성능높인다)
        
        for(let j=i+1;j<size;j++)       //j는 i의 다음값부터 계속 비교하며 같다면 둘다 0으로 변환
            if(A[i]==A[j]) A[i]=A[j]=0;
    }
    
    for(let k=0;k<size;k++)             //0이 아닌 남은 값을 return
        if(A[k]!=0)
            return A[k];
}
