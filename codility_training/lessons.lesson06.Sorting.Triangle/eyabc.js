function solution(A) {
  A.sort((a, b) => a - b);
  const aLen = A.length - 2;
  for (let i = 0 ; i < aLen; i++) {
    const a = A[i], b = A[i + 1], c = A[i+2];
    if (b > c  - a && b> a - c && - a - c < b) return 1;
    if (b > c - a) return 1;
  }
  return 0;
}
/* from sjjyy
* http://blog.daum.net/_blog/BlogTypeView.do?blogid=03OsN&articleno=13080078
*  삼각형의 세 변의 길이를 a,b,c라고 하면
    c가 가장 긴 변일 때 a + b > c (나머지 두 변의 길이의 합이 가장 긴 변의 길이보다 길다)
    그렇다면 a > c-b,  b > c-a 가 성립한다.
   또 c>0 , c > b-a (c는 b보다 길기 때문에 당연히  b-a보다 길다)이므로
     b-a < c < a + b
     c-b < a, 또는 c-a < b 가 성립한다
* */
console.log(solution([10, 2, 5, 1, 8, 20]) === 1);
console.log(solution([10, 50, 5, 1]) === 0);