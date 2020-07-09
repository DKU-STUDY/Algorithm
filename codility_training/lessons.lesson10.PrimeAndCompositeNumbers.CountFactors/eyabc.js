function solution(N) {
  let i = 1, result = 0;
  while (i * i < N) {
    if (N % i === 0) result += 2;
    i++;
  }
  return result + (i*i === N);
}

console.log(solution(24) === 8);
