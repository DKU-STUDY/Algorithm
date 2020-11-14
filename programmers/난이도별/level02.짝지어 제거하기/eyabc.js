function solution(s) {
  const len = s.length;
  const stack = [];


  for (let i = 0 ; i < len ; i++) {
    const [thisValue, nextValue] = [s[i], s[i + 1]];

    // 스택의 마지막 값과 현재 값이 같다면, 스택의 마지막값과 현재값이 사라집니다.
    if (stack[stack.length - 1] === thisValue) {
      stack.pop();
      continue;
    }

    // 현재 값과 다음 값이 다르다면 ? 현재 값을 스택에다 넣습니다 : 같다면 현재값과 다음값을 스택에다 넣지않고, 다음값의 인덱스의 검사를 건너 뜁니다.
    (thisValue !== nextValue) ? stack.push(thisValue) : (i += 1);
  }

  // 스택이 비어 있다면 1을 반환하고 스택의 길이가 있다면 0 을 반환합니다.
  return !(stack.length > 0) * 1;
}


console.log(solution('baabaa') === 1);
console.log(solution('cdcd') === 0);
