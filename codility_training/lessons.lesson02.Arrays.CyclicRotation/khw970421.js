function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)4
    const b=[];
    let size=A.length;
    for(let i=0;i<size;i++)
    {
        b[(i+K)%size]=A[i]; //b라는 곳에 자신의 값에 K만큼 옮긴것을 더한것에서 크기만큼 나눠준곳에 대입
    }
    return b;
}
