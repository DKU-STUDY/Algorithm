function solution(A, B, K) {
    if (A === B) return B % K === 0 ? 1 : 0;
    const f = ~~(B / K);
    const s = ~~(A / K) - (A % K ? 0 : 1)
    return f- s;
}

console.log(
  solution(11, 13, 2) === 1,
  solution(10, 10, 7) === 0,
  solution(0, 0, 11) === 1
)
