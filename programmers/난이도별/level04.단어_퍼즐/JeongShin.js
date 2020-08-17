// DP를 이용한 풀이

function solution(strings, t) {
    const answer = [];
    answer[-1] = 0;

    const checkStr = (str, from, to) => {
        for (let i = from, j = 0; i <= to; i++, j++) {
            if (t[i] !== str[j])
                return false;
        }
        return true;
    };

    const getCount = (char, idx) => {
        let count = Infinity;
        for (const str of strings) {
            const len = str.length;
            if (str[len - 1] === char && checkStr(str, idx - len + 1, idx))
                count = Math.min(answer[idx - len] + 1, count);
        }
        return count;
    };

    const result = t.split('').reduce((answer, char, idx) => {
        answer.push(getCount(char, idx));
        return answer;
    }, answer)[t.length - 1];

    return result === Infinity ? -1 : result;
}

// solution(["ba", "na", "n", "a"], "banana")
// solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple")

/*
* 처음 시도 했던 트라이를 이용한 풀이
* 효율성 테스트에서 불합격 ㅠㅠ 😥
* */
class TrieNode {
    constructor(key) {
        this.key = key;
        this.end = false;
        this.children = {};
    }
}

function Trie() {
    this.root = new TrieNode();
    this.insert = function (word, len = word.length) {
        let node = this.root;
        for (let i = 0; i < len; i++) {
            const curr = word[i];
            if (!node.children[curr])
                node.children[curr] = new TrieNode(curr);
            node = node.children[curr];
            if (i === (len - 1))
                node.end = true;
        }
    };
}

function solution2(strings, t) {
    const trie = new Trie();
    const target = t.length;
    let answer = Infinity;

    const find = (startIdx, weight) => {
        let node = trie.root;

        if (answer <= weight)
            return;

        if (startIdx === target)
            return answer = weight;

        for (let i = startIdx; i <= target; i++) {
            const curr = t[i];
            if (node.children[curr]) {
                node = node.children[curr];
                if (node.end)
                    find(i + 1, weight + 1);
                continue;
            }
            return
        }
    };

    for (const str of strings)
        trie.insert(str);

    find(0, 0);

    return answer !== Infinity ? answer : -1;
}
