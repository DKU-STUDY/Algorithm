function solution(arr) {
  return arr.reduce((result, present) => (result + present)) / arr.length;
}

// 문제풀이:
// 지난 번에 배웠던 reduce 함수를 통해 값을 구할 수 있었다.
// reduce의 맨 앞 값(result)은 함수 적용된 후의 함수이고, 
// present는 현재 값이다.
// 결과에 현재값을 다 더하고, array의 길이 만큼 나누면 평균값이 나온다. 