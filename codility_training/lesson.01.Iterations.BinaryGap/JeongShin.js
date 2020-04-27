function solution(N) {
  const s = N.toString(2);
  var max_gap = 0;
  var front = s.indexOf("1");
  if (front === -1) return 0;
  while (true) {
    let back = s.indexOf("1", front + 1);
    if (back === -1) break;
    let gap = back - front - 1;
    if (gap > max_gap) max_gap = gap;
    front = back;
  }
  return max_gap;
}
