function solution(A) {
    if (!A) return;
    const len = A.length;
    let P = 1;
    const arr = [];
    //reduce 가 반복문 안으로 들어가면 시간 복잡도가 n^2이 되기 때문에 빼준다.
    var diff = A[0] - A.slice(P).reduce((prev, curr) => prev + curr);
    //앞, 뒤 배열 차이를 현재 인덱스 (P) 기준으로 덧셈 뺄셈으로 계산 후 arr에 push
    while (P < len) {
        arr.push(diff);
        diff += A[P++] * 2;
    }
    return arr.reduce ((min, a)=> Math.min(Math.abs(a), min), min);
}

var ans = solution([-1000, 1000]);
console.log(ans);
