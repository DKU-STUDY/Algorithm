class Node {
    constructor(key) {
        this.key = key;
        this.children = new Map();
        this.isEnd = false;
    }
}

const WordDictionary = class {
    constructor() {
        this.root = new Node(null);
    };

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        const len = word.length;
        let node = this.root;

        for (let i = 0; i < len; i++) {
            const curr = word[i];
            if (!node.children.has(curr))
                node.children.set(curr, new Node(curr));
            node = node.children.get(curr);
        }
        node.isEnd = true;
    };

    /**
     * 단어가 Trie 에 포함 되어 있는지 판단. '.'으로 모든 단어 대체 가능
     * @param {string} word
     * @return {boolean}
     */

    search(word) {
        return find(word, 0, this.root, word.length);
    };
};

/*
   * Backtracking
   * @param {string} word
   * @param {number} idx
   * @param {Node} node
   * */
function find(word, idx, node) {
    if (idx === word.length) {
        return node.isEnd;
    }

    const curr = word[idx];

    // if (curr === '.' && node.children.values().find(child => find(word, idx + 1, child)))
    if (curr === '.')
        for (let child of node.children.values())
            if (find(word, idx + 1, child))
                return true;

    if (!node.children.has(curr))
        return false;

    return find(word, idx + 1, node.children.get(curr));
}