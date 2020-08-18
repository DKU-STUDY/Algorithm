class Node {
    constructor(key) {
        this.key = key;
        this.children = {};
    }
}

const WordDictionary = function () {
    this.forwardRoot = {};
    this.backwardRoot = {};
};

/**
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function (word) {
    const len = word.length;
    let fNode, bNode;
    fNode = this.forwardRoot[len] = (this.forwardRoot[len] || new Node(null));
    bNode = this.backwardRoot[len] = this.backwardRoot[len] || new Node(null);

    for (let i = 0, j = len - 1; i < len; i++, j--) {
        if (!fNode.children[word[i]])
            fNode.children[word[i]] = new Node(word[i]);
        fNode = fNode.children[word[i]];

        if (!bNode.children[word[j]])
            bNode.children[word[j]] = new Node(word[j]);
        bNode = bNode.children[word[j]];
    }
};

/**
 * 단어가 Trie 에 포함 되어 있는지 판단. '.'으로 모든 단어 대체 가능
 * @param {string} word
 * @return {boolean}
 */

WordDictionary.prototype.search = function (word) {
    const len = word.length;
    let node = word[0] === '.' ? this.backwardRoot[len] : this.forwardRoot[len];
    word = word[0] === '.' ? word.split('').reverse().join('') : word;

    if (!node)
        return false;

    for (let i = 0; i < len; i++) {
        const curr = word[i];
        if (curr === '.')
            return true;
        if (!node.children[curr])
            return false;
        node = node.children[curr];
    }

    return true;
};

const trie = new WordDictionary();
trie.addWord('apple');
console.log(trie.search('..le'));


