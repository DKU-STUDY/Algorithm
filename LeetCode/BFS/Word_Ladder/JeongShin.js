/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 * 시작 단어와 끝 단어가 주어질 때 하나의 단어씩 바꾸어 가면서 최소 바꾸는 경로 길이 구하기
 */
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

/* currWord 기준으로 가능한 모든 단어 스택에 푸쉬 */


/* endWord 로 가는 최단 경로 길이 반환, 방법이 없을 시 -1 반환 */
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

ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]);