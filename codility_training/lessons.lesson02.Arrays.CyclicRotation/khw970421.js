function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)4
    let b=[];
    for(let i=0;i<A.length;i++)
    {
        b[(i+K)%A.length]=A[i]; //b라는 곳에 자신의 값에 K만큼 옮긴것을 더한것에서 크기만큼 나눠준곳에 대입
    }
    return b;
}
