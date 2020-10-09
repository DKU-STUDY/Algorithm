/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
const minWindow = function (s, t) {
    const map = Array.from(t).reduce((m, v) => {
        m[v] = (m[v] || 0) + 1;
        return m
    }, {});

    let start = 0, end = 0, counter = t.length, minStart = 0, minLen = Infinity, len = s.length;
    while (end < len) {
        const char = s[end];
        console.log(char, map);

        // 만약 char 가 t안에 있다면 counter 를 줄인다.
        counter -= (map[char] > 0);
        // map 에서 해당 char 의 개수를 줄여준다.
        if (map[char] !== undefined)
            map[char]--;
        end++;
        // 만약 t 의 모든 단어를 찾은 경우
        // start 를 현재 len 범위 내에서 새로 찾는다
        while (counter === 0) {
            const startChar = s[start];
            if (end - start < minLen) {
                minStart = start;
                minLen = end - start;
            }
            if (map[startChar] !== undefined)
                map[startChar]++;
            counter += (map[startChar] > 0);
            start++;
        }
    }
    return minLen !== Infinity ? s.substring(minStart, minStart + minLen) : '';
};

console.log(minWindow("ADOBECODEBANC", "ABC"));