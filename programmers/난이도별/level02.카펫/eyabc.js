/**
 * https://programmers.co.kr/learn/courses/30/lessons/42842
 * 출처에 참고해야 할 이미지가 있습니다.
 * @param brown, 갈색 격자수 8 ~ 5000 자연수, 카펫의 테두리
 * @param yellow, 노란색 격자수 1 ~ 2000000 자연수, 카펫 테두리의 안쪽 사각형
 * @return 카펫의 {[가로크기, 세로크기]}, 가로  >= 세로
 * 완전탐색이면 모든 가로 세로의 길이 가능성을 고려하여 풀어야 한다.
 */
const initSize = (width, height) => ({ width, height });

function solution(brown, yellow) {
  const Y = initSize(yellow / 1, 1);

  while (Y.width >= Y.height) {

    Y.width = yellow / Y.height;

    const computedYellowCount = Y.width * Y.height;

    if (Number.isInteger(Y.width) && (computedYellowCount === yellow)) {

      const [width, height] = [Y.width + 2, Y.height + 2];

      if ((width * height - computedYellowCount) === brown)
        return [width, height];
    }
    Y.height += 1;
  }
}

console.log(solution(10, 2));   //	[4, 3]
console.log(solution(8, 1));  //	[3, 3]
console.log(solution(24, 24));  //	[8, 6]