/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
const canFinish = function (numCourses, prerequisites) {
    const graph = new Map();
    const visited = new Map();

    for (const [course, prerequisite] of prerequisites) {
        const courseArr = graph.get(course) || graph.set(course, []).get(course);
        courseArr.push(prerequisite);
    }

    for (const course of graph.keys()) {
        if ((numCourses = dfs(graph, course, numCourses, visited)) === false)
            return false;
    }

    return true;
};

const dfs = function (graph, course, num, visited) {
    if (visited.get(course) || num < 0)
        return false;

    visited.set(course, true);

    for (const pre of graph.get(course)) {
        if (!graph.has(pre))
            continue;
        if (!dfs(graph, pre, num, visited))
            return false;
    }

    visited.set(course, false);
    return num;
};
