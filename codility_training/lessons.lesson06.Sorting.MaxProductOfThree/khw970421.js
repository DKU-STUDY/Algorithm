function solution(A) {
    A.sort((a,b)=>b-a);
    const len=A.length;
    if(A[0]*A[1]*A[2]==0){
        return A[len-1]*A[len-2]*A[0];
    }
    if(A[len-1]*A[len-2]*A[0]==0){
        return A[0]*A[1]*A[2];
    }
    else
        return Math.min(A[0]*A[1]*A[2],A[len-1]*A[len-2]*A[0]);
}

console.log("에러);

//나열했을때 경우의수는 결국 3가지
//
// 순서로 나열했을때 제일큰수부터 3가지의 곱이 제일클때
//
// 순서로 나열했을때 제일절대값이 큰음수 2개와 제일큰 양수의 곱
//
// 그외에 제일큰수부터 계산할때 0이 포함될때, 제일작은수 2개랑 큰수 2개했을때 0이 포함될때 경우