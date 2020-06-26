function solution(begin, target, words) {
    const len = words.length;
    let ans = Infinity;

    // 일치하지 않는 알파벳 개수 반환
    const match = (str, word_idx) => {
        return str.split("").reduce((acc, curr, idx) => {
            return acc + (words[word_idx][idx] !== curr)
        }, 0);
    };
    const visited = {};

    const dfs = (start) => {
        const {word, count} = start;

        if (word === target) {
            ans = Math.min(count, ans);
            return null;
        }

        visited[word] = true;

        for (let i = 0; i < len; i++) {
            if (match(word, i) === 1 && visited[words[i]] === undefined)
                dfs({word: words[i], count: count + 1});
        }
    };

    dfs({word: begin, count: 0});

    return ans === Infinity ? 0 : ans;
}

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]);