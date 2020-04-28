function solution(X, Y, D) {
  const goal = Y - X;
  if (goal <= 0) return 0;
  else {
    return Math.floor(goal / D) + (goal % D ? 1 : 0);
  }
}
