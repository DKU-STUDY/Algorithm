/**
 * https://leetcode.com/problems/palindrome-pairs/
 * @param words  단어들의 유니크한 배열
 * @return 두 words[i] + words[j]의 연결이 회문이되도록 주어진 목록에서 고유 한 색인 (i, j)의 모든 쌍을 반환합니다.
 * 성능 개선을 위해 Trie 알고리즘 공부
 * https://brunch.co.kr/@springboot/75
 * https://www.youtube.com/watch?v=7e1b70dTAd4
 */

/*
 * https://www.youtube.com/watch?v=9nqiphzFbFc
 * 2968 ms	52 MB
 */
// 두 단어를 합쳤을 때 회귀문이 되는지 판별 한다.
const recursion = (word1, word2) => {
  const combined = word1 + word2;
  const combinedLen = combined.length;

  let a = 0;
  let b = combinedLen - 1;
  while (a < b) {
    if (combined.charAt(a) !== combined.charAt(b)) return false;
    a += 1;
    b -= 1;
  }
  return true;
};

const palindromePairs0 = function(words) {
  const result = [];
  const len = words.length;

  words.forEach((word1, i) => {
    for (let j = i + 1 ; j < len ; j++) {
      const word2 = words[j];
      if (recursion(word1, word2)) result.push([i, j]);
      if (recursion(word2, word1)) result.push([j, i]);
    }
  });
  return result;
};


// 시간 초과
const palindromePairs2 = function(words) {
  const result = [];
  words.forEach((word1, i) => {
    words.forEach((word2, j) => {
      if (i === j) return;
      const combined = word1 + word2;
      const combinedLen = combined.length;
      if (combinedLen === 1) {
        result.push([i, j]);
        return;
      }
      const isEven = (combinedLen % 2) === 0;
      let first, second;
      let middle = combinedLen / 2;
      if (isEven) {
        first = combined.slice(0, middle);
        second = [...combined.slice(middle, combinedLen)].reverse().join('');
      } else {
        middle = ~~middle;
        first = combined.slice(0, middle);
        second = [...combined.slice(middle + 1, combinedLen)].reverse().join('');
      }
      if (first === second) result.push([i, j]);
    });
  });
  return result;
};

// 시간 초과
const palindromePairs3 = function(words) {
  const result = [];

  const recursion = (word1, word2, i, j) => {
    const combined = word1 + word2;
    const combinedLen = combined.length;
    if (combinedLen === 1) {
      result.push([i, j]);
      return;
    }
    const isEven = (combinedLen % 2) === 0;
    let first, second;
    let middle = combinedLen / 2;
    if (isEven) {
      first = combined.slice(0, middle);
      second = [...combined.slice(middle, combinedLen)].reverse().join('');
    } else {
      middle = ~~middle;
      first = combined.slice(0, middle);
      second = [...combined.slice(middle + 1, combinedLen)].reverse().join('');
    }
    if (first === second) result.push([i, j]);
  };

  words.forEach((word1, i) => {
    for (let j = i + 1 ; j < words.length ; j++) {
      const word2 = words[j];
      recursion(word1, word2, i, j);
      recursion(word2, word1, j, i);
    }
  });
  return result;
};

// https://www.youtube.com/watch?v=7e1b70dTAd4
class Trie {
  head = {};

  add(word) {
    let currNode = this.head;
    for (const char of word) {
      if (currNode[char] === undefined) {
        currNode[char] = {};
      }
      currNode = currNode[char];
    }
    currNode['*'] = true;
  }

  search(word) {
    let currNode = this.head;

    for (const char of word) {
      if (currNode[char] === undefined) {
        return false;
      }
      currNode = currNode[char];
    }
    return !!currNode['*'];
  }
}

console.log(palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll']) === [[0, 1], [1, 0], [3, 2], [2, 4]]);
// console.log(palindromePairs(['bat', 'tab', 'cat']) === [[0, 1], [1, 0]]);
// console.log(palindromePairs(['a', '']) === [[0, 1], [1, 0]]);
// console.log(palindromePairs(['a', 'abc', 'aba', '']) === [[0, 3], [3, 0], [2, 3], [3, 2]]);


