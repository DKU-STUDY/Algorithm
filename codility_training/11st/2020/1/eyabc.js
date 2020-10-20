/**
 * @param S
 * @return a 가 삽입될 수 있는 최대 개수
 * a 삽입의 조건: a 가 최대 2개 연속하여 존재할 수 있다.
 * a 가 3개 이상 연속하면 -1 을 리턴한다.
 */

const notAidx = (string) => Array.from(string.matchAll('[^a]', 'g'), v => v.index);

const countInsertedA = (notAidx, originLastIdx) => {
  const notAidxLastIdx = notAidx.length - 1;

  // 첫번째 notAidx의 인덱스앞에 삽입할 수 있는 a 의 개수와, 마지막 notAidx 의 인덱스 뒤에 삽입할 수 있는 a 의 개수를 미리 구한다.
  let cnt = 4
    - notAidx[0]
    - (originLastIdx - notAidx[notAidxLastIdx]);

  notAidx.forEach((v, i) => {

    // 마지막 인덱스는 계산하지 않는다. (앞에 이미 계산함)
    if (i === notAidxLastIdx) return;

    // 현재 인덱스와 다음 인덱스 사이에 삽입할 수 있는 a 의 개수를 구한다.
    cnt += (3 - notAidx[i + 1] + v);
  });
  return cnt;
};

function solution(S) {
  if (/aaa/.test(S)) return -1;
  if (S === 'aa') return 0;

  const originLastIdx = S.length - 1;

  // a 문자가 아닌 문자들의 인덱스 배열을 반환한다.
  const found = notAidx(S);

  // 삽입된 a 개수를 리턴한다.
  return countInsertedA(found, originLastIdx);
}

console.log(solution('aabab') === 3); // aabaabaa
console.log(solution('dog') === 8); // aadaaoaagaa
console.log(solution('dogaa') === 6); // aadaaoaagaa
console.log(solution('aa') === 0); // aa
console.log(solution('baaaa') === -1); // -1
console.log(solution('baabaa') === 2); //
console.log(solution('aabaa') === 0); //
