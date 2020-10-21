/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
const findOrder = function (numCourses, prerequisites) {
    const graph = new Map();
    const visited = new Map();
    const answer = [];

    for (const [course, prerequisite] of prerequisites) {
        const courseArr = graph.get(course) || graph.set(course, []).get(course);
        courseArr.push(prerequisite);
    }

    for (let i = 0; i < numCourses; i++) {
        if (dfs(graph, i, numCourses, visited, answer) === false)
            return [];
    }
    return answer;
};

const dfs = function (graph, course, num, visited, answer) {
    // 싸이클이 발생한 경우
    if (visited.get(course) === -1)
        return false;
    // 이미 들은 과목인 경우 스킵
    if (visited.get(course) === 1)
        return true;
    // 현재 과목 수강
    visited.set(course, -1);

    if (graph.has(course)) {
        for (const pre of graph.get(course)) {
            if (dfs(graph, pre, num - 1, visited, answer) === false)
                return false;
        }
    }

    visited.set(course, 1);
    answer.push(course);
    return true;
};

