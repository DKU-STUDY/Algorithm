/*
* @eyabc 님 풀이 참고했습니다. 이렇게 짧게 구현이 가능하네요 ㅠ
* */
function solution(A) {
    const len = A.length;
    if (len < 4)
        return A.reduce((acc, curr) => curr * acc, 1);
    A.sort((a, b) => a - b);
    return Math.max(A[0] * A[1] * A[len - 1], A[len - 1] * A[len - 2] * A[len - 3]);
}
// 원래 시도하려 했던 방법
// for (const val of A)
//     val >= 0 ? pos.push(val) : neg.push(val);
// pos.sort((a, b) => b - a);
// neg.sort((a, b) => a - b);
// const neg_len = neg.length;
// return pos.length === 0 ? neg[neg_len - 1] * neg[neg_len - 2] * neg[neg_len - 3] :
//     Math.max(number(pos[0]) * number(pos[1]) * number(pos[2]), number(pos[0]) * number(neg[0]) * number(neg[1]),
//     );

