// 2020.08.25 코드 복습 및 수정
class Node {
    constructor(key) {
        this.key = key;
        this.count = 0;
        this.children = new Map();
    }
}

class Trie {
    constructor() {
        this.root = new Node(null);
    }

    // @param {boolean} reverse : 단어를 거꾸로 넣을 것인지 (true) 순서대로 넣을 것인지 (false)
    insert(word, reverse, len) {
        let node = this.root;
        for (let i = 0; i < len; i++) {
            const curr = word[reverse ? len - i - 1 : i];
            if (!node.children.has(curr))
                node.children.set(curr, new Node(curr));
            node = node.children.get(curr);
            node.count = (node.count || 0) + 1;
        }
    }

    search(word, reverse, len = word.length, node = this.root) {
        for (let i = 0; i < len; i++) {
            const curr = word[reverse ? len - i - 1 : i];
            node = node.children.get(curr);
            if (!node)
                return 0;
        }
        return node.count;
    }
}

function solution(words, queries) {
    const regEx = /\?/g;
    const [forward, backward, exceptions] = words.reduce(([f, b, e], word) => {
        const len = word.length;
        [f[len], b[len]] = [f[len] || new Trie(), b[len] || new Trie()];
        f[len].insert(word, false, len);
        b[len].insert(word, true, len);
        e[len] = (e[len] || 0) + 1;
        return [f, b, e];
    }, [{}, {}, {}]);

    return queries.map((query) => {
        const len = query.length;
        const str = query.replace(regEx, '');
        if (!forward[len])
            return 0;
        if (query[0] === '?' && query[len - 1] === '?')
            return exceptions[len];
        if (query[0] === '?')
            return backward[len].search(str, true);
        return forward[len].search(str, false);
    })
}

