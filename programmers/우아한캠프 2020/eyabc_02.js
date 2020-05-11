function solution (arr) {
  const res = arr.map(v => [...(v+'')].sort((a, b) => a -b).join('') );
  return new Set(res).size;
}

console.log(
  solution([112, 1814, 121, 1481, 1184])===	2,
  solution([123, 456, 789, 321, 654, 987])===	3,
  solution([1, 2, 3, 1, 2, 3, 4])===	4,
  solution([123, 234, 213, 432, 234, 1234, 2341, 12345, 324])===	4,
)