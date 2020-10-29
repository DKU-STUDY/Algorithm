class Node {
    constructor(word, count) {
        this.word = word;
        this.count = count;
    }
}

class PriorityQueue {
    constructor() {
        this.items = [];
        this.length = 0;
    }

    enqueue(word, count) {
        let node = new Node(word, count);
        let contain = false;
        for (let i = 0; i < this.length; i++) {
            if (this.items[i].count >= node.count) {
                i -= this.items[i].count === node.count ? (this.items[i].word < node.word) : 0;
                this.items.splice(i, 0, node);
                contain = true;
                break;
            }
        }

        if (!contain)
            this.items.push(node);
        this.length++;

    }
}

/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
const topKFrequent = function (words, k) {
    const wordCount = new Map;
    const answer = [];
    const queue = new PriorityQueue();

    for (const word of words)
        wordCount.set(word, (wordCount.get(word) || 0) + 1);

    for (const [word, count] of wordCount.entries())
        queue.enqueue(word, count);

    for (let i = 0; i < k; i++)
        answer.push(queue.items.pop().word);

    return answer;
};


topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2); // ["i", "love"]


