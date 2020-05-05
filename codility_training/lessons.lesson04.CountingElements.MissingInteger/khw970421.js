function solution(A) {
    A.sort((a,b)=>a-b);         //오름차순 정렬
    const size = A.length;
    for(let i=1;i<size+2;i++)   //1부터 전체 크기가 [1,2,3]일때 전부 반복하며 다음크기를 찾아야하므로 저렇게 설정
    {
        if(A.indexOf(i)<0)
            return i;
    }
}

console.log(
    solution([-2,-2,0,1,2,3,5,6,7])===4
)