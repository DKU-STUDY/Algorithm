/* Solution 2. 효율성 불합격 */
// function solution2(words, queries) {
//     return queries.map((query) => {
//         const regEx = '^' + query.replace(/\?/g, '.') + '$';
//         const filtered = words.reduce((acc, curr) => {
//             const r = curr.match(regEx);
//             if (r)
//                 acc.add(r);
//             return acc;
//         }, new Set());
//         return filtered.size;
//     })
// }

// Solution 1. Trie 자료구조로 풀이

class TrieNode {
    constructor(key) {
        this.key = key;
        this.count = 0;
        this.children = {};
    };
}

const Trie = function (type) {
    this.root = new TrieNode();
    this.type = type;
    this.insert = function (word, target, idx, node = this.root) {
        while (idx !== target) {
            const curr = word[idx];
            if (!node.children[curr]) {
                node.children[curr] = new TrieNode(curr);
            }
            node.count++;
            node = node.children[curr];
            this.type ? idx++ : idx--;
        }
    };

    this.find = function (word, len = word.length) {
        let node = this.root;
        let idx = 0;
        while (idx < len) {
            const curr = word[idx];
            if (!node.children[curr]) {
                return 0;
            }
            node = node.children[curr];
            idx++;
        }
        return node.count;
    }
};

const reverse = function (str) {
    return str.split('').reduce((reversed, character) => character + reversed, '')
};

function solution(words, queries) {
    const forward = {}, backward = {}, exceptions = {};

    for (const word of words) {
        const len = word.length;
        exceptions[len] = (exceptions[len] || 0) + 1;
        forward[len] = forward[len] || new Trie(true);
        backward[len] = backward[len] || new Trie(false);
        forward[len].insert(word, len, 0);
        backward[len].insert(word, -1, len - 1);
    }

    return queries.map((el)=> {
        const len = el.length;
        const str = el.replace(/\?/g, '');
        if (!forward[len] || !backward[len])
            return 0;
        if (el[len - 1] ==='?' && el[0] ==='?')
            return exceptions[len];
        if (el[len - 1] ==='?')
            return forward[len].find(str);
        if (el[0]=== '?')
            return backward[len].find(reverse(str));
    });
}

console.log(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "?????", "fr???", "fro???", "pro?"]))
