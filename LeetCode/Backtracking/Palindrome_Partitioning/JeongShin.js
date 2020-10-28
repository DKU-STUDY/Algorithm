/**
 * @param {string} s
 * @return {string[][]}
 */
const partition = function (s) {
    const target = s.length;
    const answer = [];
    let possibleAnswer = [];
    backtracking(s, 0, s.length, possibleAnswer, answer);
    return answer;
};

function checkPalindrome(string, startIdx, endIdx) {
    while (startIdx < endIdx) {
        if (string[startIdx++] !== string[endIdx--])
            return false;
    }
    return true;
}

function backtracking(string, startIdx, target, possibleAnswer, answer) {
    if (startIdx === target){
        return answer.push([...possibleAnswer]);
    }
    for (let endIdx = startIdx; endIdx < target; endIdx++) {
        if (checkPalindrome(string, startIdx, endIdx)) {
            possibleAnswer.push(string.substring(startIdx, endIdx + 1));
            backtracking(string, endIdx + 1, target, possibleAnswer, answer);
            possibleAnswer.pop();
        }
    }
}

partition("aab"); // ["aa", "b"], ["a","b", "c"]