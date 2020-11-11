const balancedStringSplit = function (s) {
  let [R, L, cnt] = [0, 0, 0];

  Array.from(s, (char) => {
    (char === 'R') ? (R += 1) : (L += 1);
    (R === L) && ([R, L, cnt] = [0, 0, cnt + 1]);
  });
  return cnt;
};

console.log(balancedStringSplit('RLRRLLRLRL') === 4);
console.log(balancedStringSplit('RLLLLRRRLR') === 3);
console.log(balancedStringSplit('LLLLRRRR') === 1);
console.log(balancedStringSplit('RLRRRLLRLL') === 2);