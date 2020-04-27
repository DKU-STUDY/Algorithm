function solution (X, A) {
  const set = new Set();
  const len = A.length();

  for (let i = 0; i < len; i++) {
    set.add(A[i]);
    if(set.size === X) return i;
  }
  return -1;
}

console.log(
  solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) === 6,
  solution(5, [1, 1, 1, 1, 2, 3, 4, 5]) === 7,
);

// timeout
function solution2 (X, A) {
  let time = -1;
  let count = 0;
  const locateArr = [];
  const f = () => {
    if (locateArr.includes(count + 1)) {
      count++;
      f();
    }
    return;
  };
  while (count < X) {
    time++;
    locateArr.push(A.shift());
    f();
  }
  return time;
}

// spent : Array.prototype.includes > indexOf
function solution2 (X, A) {
  let time = -1;
  let location = 0;
  if (A.length < X) return -1;

  while (location < X) {
    const newLocation = A.indexOf(++location);
    if (newLocation === -1) return -1;
    else if (newLocation > time) {
      time = newLocation;
    }
  }
  return time;
}
