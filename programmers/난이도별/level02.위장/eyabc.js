/**
 * https://programmers.co.kr/learn/courses/30/lessons/42578?language=javascript
 * 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
 * @param clothes 스파이가 가진 의상들이 담긴 2차원 배열
 * @return 서로 다른 옷의 조합의 수
 clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
 같은 이름을 가진 의상은 존재하지 않습니다.
 clothes의 모든 원소는 문자열로 이루어져 있습니다.
 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
 스파이는 하루에 최소 한 개의 의상은 입습니다.
 */
function solution(clothes) {

  // hash = { headgear: 2, eyewear: 1 }, 키 (의상의 분류), value: 의상의 개수
  const hash = clothes.reduce((hash, [cloth, kind]) => {
    hash[kind] = (hash[kind] || 0) + 1;
    return hash;
  }, {});

  // (2 + 1) * ( 1 + 1 ) = 4 : 1 을 더하는 이유는 의상의 분류에서 아무옷도 선택하지 않는 경우의 수도 추가 하였기 때문이다.
  // 4 - 1 : 1을 빼는 것은 위 경우의 수에서 모든 의상 분류에서 아무것도 입지 않았을 경우의 수도 count 하였기 때문임
  return Object.values(hash)
               .reduce((ans, value) => ans *= (value + 1), 1)
    - 1;
}

console.log(
  solution([['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]) === 3,
  solution([['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]) === 3,
  solution([['crow_mask', 'face'], ['blue_sunglasses', 'face']]) === 2,
  solution([['crow_mask', 'face']]) === 1,
);



