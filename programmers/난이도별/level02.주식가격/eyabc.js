/**
 * https://programmers.co.kr/learn/courses/30/lessons/42584
 * @param prices 초 단위로 기록된 주식가격이 담긴 배열
 * @return 가격이 떨어지지 않은 기간은 몇 초인지를 return
 prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
 prices의 길이는 2 이상 100,000 이하입니다.


 https://programmers.co.kr/questions/12172
 예로 [1, 2, 3, 2, 3, 3, 1]의 결과값은 [6, 5, 1, 3, 2, 1, 0]이 나와야합니다.
 1 : 2, 3, 2, 3, 3, 1 -> 6초간 떨어지지 않으니 결과값 6
 2 : 3, 2, 3, 3, 1 -> 5초간 떨어지지 않으니 결과값 5
 3 : 2 -> 1초 뒤에 떨어지니 기대값 1
 (이부분에서 1초간 떨어지니 결과값을 3으로 생각했었습니다.)
 2 : ~~ 결과값 3
 3 : ~~ 결과값 2
 3 : ~~ 결과값 1
 1 : 결과값 0

 */
function solution(prices) {
  const len = prices.length;
  return prices.map((price, i) => {
    for (let j = i + 1 ; j < len ; j++)
      if (prices[j] < price) return j - i;
    return len - 1 - i;
  });
}

console.log(solution([1, 2, 3, 2, 3])); // [4, 3, 1, 1, 0]
console.log(solution([1, 2, 3, 2, 3, 1])); //  [ 5, 4, 1, 2, 1, 0 ]
console.log(solution([3, 1])); // [ 1, 0 ]
console.log(solution([1, 2, 3, 2, 3, 3, 1])); //[6, 5, 1, 3, 2, 1, 0]
