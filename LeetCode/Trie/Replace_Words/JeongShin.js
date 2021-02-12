class Node {
  constructor(key) {
    this.key = key;
    this.children = new Map();
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new Node(null);
  }

  addWord(word, node = this.root) {
    for (const char of word) {
      if (!node.children.has(char)) {
        node.children.set(char, new Node(char))
      }
      node = node.children.get(char);
    }
    node.isEnd = true;
  }

  findAndReplaceWord(word, node = this.root) {
    let path = '';
    for (const char of word) {
      if (!node.children.has(char))
        return word;
      node = node.children.get(char);
      path += char;
      if (node.isEnd)
        return path;
    }
    return word;
  }


}

const replaceWords = function (dictionary, sentence) {
  const trie = new Trie();

  for (const word of dictionary)
    trie.addWord(word);

  return sentence.split(' ').map((word) => trie.findAndReplaceWord(word)).join(' ');
};

replaceWords(['cat', 'bat', 'rat'], 'the cattle was rattled by the battery');
