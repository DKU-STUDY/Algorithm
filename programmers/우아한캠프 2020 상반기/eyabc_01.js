function solution(A) {
  if(A.length === 1) return 1;
  let res = 1;

  const f = (arr) => {
    let curr = arr[0];
    const len = arr.length;
    let cnt = 0;
    const newArr = [];
    for(let i = 0 ; i < len + 1 ; i++) {
      if(curr === arr[i]) cnt++;
      else {
        curr = arr[i];
        newArr.push(cnt);
        cnt = 1;
      }
    }
    res++;
    if (newArr.length === 1) return;
    f([...newArr])
  };
  f([...A]);
  return res;
}

console.log(
  solution([1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]	) === 6,
  solution([1,2,3]	) === 3,
  solution([2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 2, 1, 2]	) === 5,
  solution([2]	) === 1,
)
