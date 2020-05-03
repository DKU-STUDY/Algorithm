function solution(A) {
     const size = A.length;                 //A의 크기 const로 저장
     var mySet = new Set();                 //Set 객체 챗엇
      for(let i=0;i<size;i++)             //크기만큼 반복
    {       
        if(mySet.has(A[i])==false)mySet.add(A[i]);      //A[i]가 존재하지않으면 A[i]를 mySet에 추가
        else mySet.delete(A[i]);                        //A[i]가 존재하면 A[i]를 mySet에서 제거
    }
    
    return [...mySet][0];                               //그후 남은 [0]의 set을 배열로 바꿔 return
}
