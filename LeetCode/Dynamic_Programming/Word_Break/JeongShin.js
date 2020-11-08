class Node {
    constructor(key) {
        this.children = new Map();
        this.key = key;
        this.isEnd = false;
    }
}

class Trie {
    constructor() {
        this.root = new Node(null);
    }

    addWord(word, node = this.root) {
        for (const char of word) {
            if (!node.children.has(char))
                node.children.set(char, new Node(char));
            node = node.children.get(char);
        }
        node.isEnd = true;
    }

    /**
     * @param {string} word
     * @param {number} startIdx word 의 substring 중 탐색을 시작할 인덱스
     * @param {number} endIdx word 의 substring 중 탐색이 끝나는 인덱스
     * @param {Object} node
     * @return {boolean}
     */
    findWord(word, startIdx, endIdx, node = this.root) {
        for (let i = startIdx; i < endIdx; i++) {
            const char = word[i];
            node = node.children.get(char);
            if (!node)
                return false;
        }
        return node.isEnd;
    }
}


/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
const wordBreak = function (s, wordDict) {
    const len = s.length;
    const trie = new Trie();
    const answer = {0: true};

    for (const word of wordDict) {
        trie.addWord(word);
    }

    for (let endIdx = 1; endIdx <= len; endIdx++) {
        for (let startIdx = 0; startIdx < endIdx; startIdx++) {
            if (answer[startIdx] && trie.findWord(s, startIdx, endIdx)) {
                if (endIdx === len)
                    return true;
                answer[endIdx] = true;
                break;
            }
        }
    }

    return false;
};

