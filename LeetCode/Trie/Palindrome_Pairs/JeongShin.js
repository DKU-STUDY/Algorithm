const isPalindrome = function (word, start, end) {
    while (start < end) {
        if (word[start++] !== word[end--])
            return false;
    }
    return true;
};

/*
* index : word 에서의 index 를 가집니다. 단어의 끝에는 양수의 words 에서의 word 인덱스를 가집니다.
* children : trie 자료구조에서 자식 노드.
* palindromeList : 단어 처음 ~ 현재 까지 palindrome 리스트.
* */
class Node {
    constructor(key) {
        this.key = key;
        this.index = -1;
        this.children = new Map();
        this.palindromeList = [];
    }
}

class Trie {
    constructor() {
        this.root = new Node(null);
    }

    // trie 에 word 를 삽입 합니다. 이때 단어가 역순으로 삽입 됩니다.
    addWord(word, idx, node = this.root) {
        const len = word.length;
        for (let i = len - 1; i >= 0; i--) {
            const char = word[i];
            if (!node.children.has(char))
                node.children.set(char, new Node(char));
            // 0 ~ i 까지의 substring 이 palindrome 에 해당되는지 확인 합니다. i/2 의 cost가  발생 합니다.
            // ex) 'sssll' 을 저장할 때 'llsss' 의 순서대로 삽입 되는데 'sss' 부분은 항상 palindrome 을 만족하기 때문에
            // 'll' 으로 시작하는 모든 단어들은 pair 가 가능합니다. 따라서 'll'과 같이 단어 prefix 가 일치 하는 단어들의 pair 를 찾아주기 위해 리스트 형태로 저장해 둡니다.
            if (isPalindrome(word, 0, i))
                node.palindromeList.push(idx);
            node = node.children.get(char);
        }
        node.palindromeList.push(idx);
        node.index = idx;
    }

    // 현재 단어 word 와 words 에서의 idx 를 기준으로 palindrome 을 만들 수 있는 pair 를 찾습니다.
    findPair(word, idx, answer, node = this.root) {
        const len = word.length;
        for (let i = 0; i < len; i++) {
            // 현재 탐색중인 노드가 words 에 존재 하는 단어이고 && 현재 고려중인 단어가 아니고 && i ~ 단어 끝까지 palindrome 에 해당되는지 검사합니다.
            // 단어가 역순으로 저장되어 있기 때문에 앞으로 오는 단어가 모두 palindrome 을 만족해야 합니다.
            // ex) 'sssll' 이 's' 를 탐색할 때 's' 이후에 substring 'ssll' 이 palindrome 이 따져봐야 합니다.
            if (node.index >= 0 && node.index !== idx && isPalindrome(word, i, word.length - 1))
                answer.push([idx, node.index]);

            node = node.children.get(word[i]);
            if (!node)
                return;
        }

        // 현재 단어를 끝까지 탐색하고 나서도 palindrome 을 만들 수 있는 경우
        // ex) 현재 단어 'lls' 의 경우 이전에 palindromeList 에 저장해주었던 'sssll' 과 같이 prefix 가 일치하는 단어를 찾아 push 해줍니다.
        answer.push(...node.palindromeList.filter(pairIdx => idx !== pairIdx).map((pairIdx) => [idx, pairIdx]));
    }
}

/**
 * @param {string[]} words
 * @return {number[][]}
 */
const palindromePairs = function (words) {
    const len = words.length;
    const trie = new Trie();
    const answer = [];

    for (let i = 0; i < len; i++)
        trie.addWord(words[i], i);

    for (let i = 0; i < len; i++)
        trie.findPair(words[i], i, answer);

    return answer;
};

palindromePairs(["bat", "tab", "cat"]);
palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]);
palindromePairs(["aaa", ""]);

