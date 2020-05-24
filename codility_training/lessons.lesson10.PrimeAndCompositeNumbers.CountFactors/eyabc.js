function solution(N) {
  let i = 1, result = 0;
  while (i * i < N) {
    if (N % i === 0) result += 2;
    i++;
  }
  if (i*i === N) result++;
  return result;
}

console.log(solution(24) === 8);