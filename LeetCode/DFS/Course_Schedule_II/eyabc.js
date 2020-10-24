/**
 * https://leetcode.com/problems/course-schedule-ii/
 *
 * @param {number} numCourses 코스의 개수 (인덱스 0 ~ (n-1))
 * @param {number[a][b]} prerequisites a 가 선수과목 b 가 후수과목
 *
 * @return {number[]} 모든 과정을 마치기 위해 수강해야 하는 과정의 순서.
 *  모든 과정을 마칠 수 없는 경우 빈 배열을 반환한다. (사이클이 있을경우 / 과정들의 순서가 없을 경우)
 */
  // 정점의 before 의 수와 다음 정점 after 를 가지고 있는 배열을 반환한다.
const getVertex = (hash, vertex) => {
    return hash[vertex] ? hash[vertex]
      : hash[vertex] = {
        before: 0,
        after: [],
      };
  };

const getDegree = (prerequisites) => (
  prerequisites.reduce((hash, [preVertex, postVertex]) => {
    const pre = getVertex(hash, preVertex);
    const post = getVertex(hash, postVertex);
    pre.after.push(postVertex);
    post.before += 1;
    return hash;
  }, {})
);

// numCourses 이 3 일 경우 [2, 1, 0] 혹은 [0, 1, 2] 순서로 수강하게 된다.
const noPrerequisites = (numCourses) => {
  const answer = [];
  for (let i = 0 ; i < numCourses ; i++)
    answer.push(i);
  return answer;
};

const pushQueue = (queue, check, answer, key) => {
  queue.push(key);
  check[key] = true;
  answer.push(key);
};

const initQueue = (hash, check, answer) => (
  Object.entries(hash)
        .reduce((queue, [key, { before }]) => {
          if (before === 0)
            pushQueue(queue, check, answer, Number(key));
          return queue;
        }, [])
);

// 80 ms	43.4 MB
const findOrder = function(numCourses, prerequisites) {
  // prerequisites 이 [] 비었을 때 수강하는 순서
  if (prerequisites.length === 0)
    return noPrerequisites(numCourses);

  // 1. 정점 별 진입차수를 담고 있는 hash
  const hash = getDegree(prerequisites);

  // 2. 정점의 방문을 check 하는 배열
  const check = new Array(numCourses).fill(false);

  const answer = [];

  // before 가 0 인것. 첫 시작 정점이 될 수 있는 키들 queue 에 넣는다.
  const queue = initQueue(hash, check, answer);
  // before 가 0 인 것이 없는 배열, queue: [] 은 사이클이 존재하는 것이다.
  if (queue.length === 0) return [];

  // 큐가 빌때까지 반복
  while (queue.length > 0) {
    const shifted = queue.shift();
    hash[shifted].after.forEach((vertex) => {

      // 연결되어 있던 간선을 다 제거해 준다.
      hash[vertex].before -= 1;

      if (hash[vertex].before !== 0) return;
      pushQueue(queue, check, answer, vertex);
    });
  }

  const test = !check.some((c, k) => {
    // hash[k] === undefined 은 선후수 과목에 포함되지 않는 과목을 의미한다.
    if (hash[k] === undefined) answer.push(k);
    // 선후수 과목에도 포함되어 있지만(hash[k]) 방문하지 않은 과목은(c: false) 가 남아 있으면 과목전체를 수강하지 않았다는 의미
    return !c && hash[k];
  });
  return !test ? [] : answer.reverse();
};

console.log(findOrder(2, [[1, 0]])); //[0,1]
console.log(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])); // [0,2,1,3]
console.log(findOrder(1, [])); // [0]
console.log(findOrder(2, [])); // [1, 0]
console.log(findOrder(2, [[0, 1], [1, 0]]));
console.log(findOrder(3, [[1, 0]])); // [2,0,1]
console.log(findOrder(3, [[1, 0], [2, 0]])); // [0,2,1]