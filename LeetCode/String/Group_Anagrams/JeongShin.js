/**
 * @param {string[]} strings
 * @return {string[][]}
 */
const groupAnagrams = function (strings) {
    const answer = [];
    const map = new Map();
    const charOffSet = "a".charCodeAt(0);

    for (const string of strings) {
        const charCount = new Array(26).fill(0);
        for (const char of string)
            charCount[char.charCodeAt(0) - charOffSet]++;
        const val = charCount.join(",");
        let index;
        // index 가 0 인 경우 고려하여 undefined 와 비교
        if ((index = map.get(val)) !== undefined) {
            answer[index].push(string);
            continue;
        }
        map.set(val, index = answer.length);
        answer[index] = [string];
    }
    return answer;
};


