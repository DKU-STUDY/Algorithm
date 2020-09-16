/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */

// 나의 처음 풀이 👉 시간 초과
const ladderLength = function (beginWord, endWord, wordList) {
    const graph = {};
    const len = beginWord.length;
    wordList.push(beginWord);

    for (const currWord of wordList) {
        graph[currWord] = graph[currWord] || [];
        for (const nextWord of wordList) {
            let difference = 0;
            for (let i = 0; i < len; i++)
                difference += (currWord[i] !== nextWord[i]);

            if (difference === 1)
                graph[currWord].push(nextWord)
        }
    }
    return bfs(graph, beginWord, endWord)
};

const bfs = function (graph, beginWord, endWord) {
    const visited = new Map();
    visited.set(beginWord, true);

    const stack = [{word: beginWord, count: 1, visited: visited}];
    let answer = Infinity;

    while (stack[0]) {
        const {word, count, visited} = stack.pop();

        if (word === endWord) {
            answer = Math.min(answer, count);
            continue;
        }

        if (!graph[word])
            continue;

        graph[word].forEach((nextWord) => {
            if (!visited.has(nextWord)) {
                const visitedCopy = new Map(visited);
                visitedCopy.set(nextWord, true);
                stack.push({word: nextWord, count: count + 1, visited: visitedCopy});
            }
        })
    }
    return answer === Infinity ? 0 : answer;
};

// 그래프를 사용하지 않는 풀이

const ladderLength2 = function (beginWord, endWord, wordList) {
    return wordList.includes(endWord) ? bfs(beginWord, endWord, wordList) : 0;
};

function bfs(beginWord, endWord, wordList) {
    const listLen = wordList.length;
    const wordLen = beginWord.length;
    const visited = new Array(listLen).fill(true);
    let queue = [];

    queue.push({word: beginWord, count: 1});

    while (queue[0]) {
        const {word, count} = queue.pop();
        if (word === endWord)
            return count;

        for (let i = 0; i < listLen; i++) {
            if (!visited[i])
                continue;

            let difference = 0;

            for (let j = 0; j < wordLen; j++)
                difference += (wordList[i][j] !== word[j]);

            if (difference === 1) {
                queue.unshift({word: wordList[i], count: count + 1});
                visited[i] = false;
            }
        }
    }
    return 0;
}
