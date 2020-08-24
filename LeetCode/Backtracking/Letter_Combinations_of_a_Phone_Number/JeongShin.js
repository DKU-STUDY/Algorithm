/**
 * 다음과 같이 숫자 별로 해당 문자가 정해져 있을때, (아래 chars 객체 참고)
 * digits 이 '23' 이면 2,3 으로 만들수 있는 모든 string 을 만드는 문제
 * 따라서, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] 을 반환 해야함.
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = function (digits) {
    const letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    };

    const target = digits.length;
    const answer = [];

    if (target === 0)
        return answer;

    const permutation = (str, idx) => {
        if (idx === target)
            return answer.push(str);

        letters[digits[idx]].forEach((ch) => {
            permutation(str + ch, idx + 1);
        })
    };

    permutation('', 0);

    return answer;
};