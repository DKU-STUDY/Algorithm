// https://www.youtube.com/watch?v=7e1b70dTAd4
class Trie {
  constructor() {
  }
  head = {};

  add(word) {
    let currNode = this.head;
    for (const char of word) {
      if (currNode[char] === undefined) {
        currNode[char] = {}
      }
      currNode = currNode[char];
    }
    currNode['*'] = true;
  }

  search(word) {
    let currNode = this.head;

    for(const char of word) {
      if (currNode[char] === undefined) {
        return false;
      }
      currNode = currNode[char];
    }
    return !!currNode['*'];
  }
}

const dic = new Trie();
dic.add('hi');
dic.add('abc');
dic.add('abcasasa');
console.log(dic.search('ac'));
console.log(dic.search('ab'));