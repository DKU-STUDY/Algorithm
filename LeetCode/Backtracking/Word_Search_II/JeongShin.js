class Node {
    constructor(key) {
        this.key = key;
        this.children = new Map();
        this.isEnd = null;
    }
}

class Trie {
    constructor(row, col) {
        this.root = new Node(null);
        this.row = row;
        this.col = col;
    }

    addWord(word, node = this.root) {
        const l = word.length;
        for (let i = 0; i < l; i++) {
            const curr = word[i];
            if (!node.children.has(curr))
                node.children.set(curr, new Node(curr));
            node = node.children.get(curr);
        }
        node.isEnd = word;
    }

    checkOutOfBound = (i, j) => (i >= this.row || i < 0 || j >= this.col || j < 0);

    find(board, i, j, answer, node = this.root) {
        if (this.checkOutOfBound(i, j))
            return false;

        const char = board[i][j];
        const child = node.children.get(char);

        if (char === '#' || !child)
            return;

        if (child.isEnd) {
            answer.add(child.isEnd);
            child.isEnd = null;
        }

        board[i][j] = '#';
        this.find(board, i - 1, j, answer, child);
        this.find(board, i + 1, j, answer, child);
        this.find(board, i, j + 1, answer, child);
        this.find(board, i, j - 1, answer, child);
        board[i][j] = char;
    }
}


/**
 * board 에 있는 단어들을 상, 하, 좌, 우 탐색하여
 * words 배열안에 있으면 해당 단어를 반환 하는 문제
 * @param {string[][]} board
 * @param {string[]} words
 * @return {string[]}
 */
const findWords = function (board, words) {
    const answer = new Set();
    const [row, col] = [board.length, board[0].length];
    const trie = new Trie(row, col);
    const root = trie.root.children;

    for (const word of words)
        trie.addWord(word);

    for (let i = 0; i < row; i++)
        for (let j = 0; j < col; j++)
            if (root.has(board[i][j]))
                trie.find(board, i, j, answer);

    return Array.from(answer);
};

findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"]);

findWords([["a", "b"], ["c", "d"]],
    ["ab", "cb", "ad", "bd", "ac", "ca", "da", "bc", "db", "adcb", "dabc", "abb", "acb"]);
