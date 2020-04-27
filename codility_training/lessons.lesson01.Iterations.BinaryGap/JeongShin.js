function solution(N) {
  var s = "";
  while (N != 0) {
    let add = N % 2;
    s = add.toString().concat(s);
    N = Math.floor(N / 2);
  }
  var gap = 0;
  var max_gap = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] == "1") {
      if (gap > max_gap) max_gap = gap;
      gap = 0;
    } else gap++;
  }
  return max_gap;
}
