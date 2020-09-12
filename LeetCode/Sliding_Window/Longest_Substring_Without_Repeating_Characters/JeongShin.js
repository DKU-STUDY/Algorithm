/**
 * @param {string} s
 * @return {number}
 * 가장 긴 substring 을 중복 없이 구하는 문제
 * s = "abcabcbb" 일 경우
 * "abc" 3 을 반환해야 한다.
 *
 * s = "bbbb" 일 경우
 * "b" 1 을 반환해야 한다.
 *
 * s = "pwwkew" 일 경우
 * "wke" 3 을 반환해야 한다. "pwke" 는 subsequence 이지 substring 이 아니다.
 */

const lengthOfLongestSubstring = function (s) {
    let answer = 0;
    let window = [];
    let idx;

    for (const char of s) {
        if (!~(idx = window.indexOf(char))) {
            window.push(char);
            continue;
        }
        answer = Math.max(answer, window.length);
        window = window.splice(idx + 1);
        window.push(char);
    }
    answer = Math.max(answer, window.length);
    return answer;
};

lengthOfLongestSubstring("ohvhjdml");
