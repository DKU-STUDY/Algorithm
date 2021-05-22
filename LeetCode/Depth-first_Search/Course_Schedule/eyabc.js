/**
 * https://leetcode.com/problems/course-schedule/
 * @param numCourses : courses you have to take / 들을 수 있는 course 의 수
 *   코스의 라벨은 0 부터 numCourses - 1 까지임.
 * @param prerequisites 선수 과목을 담고 있는 배열
 *    [0,1] : 0 이 1의 선수 과목임
 * @return 모든 코스를 수강을 할 수 있으면 true 리턴
 *
 * Topological Sort 위상 정렬을 이용해 풀 수 있다.
 * https://blog.naver.com/ndb796/221236874984
 * 순서가 정해져 있는 작업을 차례로 수행해야 할 때 그 순서를 결정해 주기 위해 사용하는 알고리즘
 * 사이클이 발생하지 않는 방향 그래프에서만 가능하다. 사이클이 있으면 시작점을 찾을 수 없기 때문.
 *
 * 후기: topology 알고리즘 이라는 힌트를 얻어서 아이디어는 쉽게 얻을 수 있었으나 대부분의 테스트 케이스에서 오답이 나왔다.
 * 테스트 케이스를 보고 알고리즘을 수정하였습니다.
 */

// 정점별 진입차수 count
const inDegree = (prerequisites) => (
  prerequisites.reduce((hash, prerequisite) => {

    prerequisite.forEach((vertex, j) => {

      // 초기화
      if (!hash[vertex]) {
        const vertexObj = hash[vertex] = {};
        vertexObj.after = [];
        vertexObj.before = 0;
      }

      const vertexObj = hash[vertex];
      const [before, after] = [prerequisite[j - 1], prerequisite[j + 1]];
      after !== undefined && vertexObj.after.push(after);
      before !== undefined && (vertexObj.before += 1);
    });
    return hash;
  }, {})
);

const canFinish = function(numCourses, prerequisites) {
  if (prerequisites.length === 0) return true;

  /*
   {
   '0': { after: [], before: 2 },
   '1': { after: [ 0 ], before: 0 },
   '2': { after: [ 0 ], before: 0 }
   }
   */
  const hash = inDegree(prerequisites);

  // 정점의 방문을 check 한다.
  const check = new Array(numCourses).fill(false);

  let queue = [];

  // 진입차수가 0 인 것(before 가 없는것) 을 큐에 넣고 방문처리 한다..
  // { queue: [ '1', '2' ], check: [ false, true, true ] }
  Object.entries(hash).forEach(([key, { before }]) => {
    if (before !== 0) return;
    queue.push(key);
    check[key] = true;
  });

  // 큐가 빌때까지 반복
  while (queue.length > 0) {

    // 큐에서 꺼낸다음.
    const shifted = queue.shift();
    hash[shifted].after.forEach((vertex) => {

      // 연결되어 있던 간선을 다 제거해 준다.
      hash[vertex].before -= 1;

      // 진입차수가 0 인 것을 큐에 넣고 반복처리
      if (hash[vertex].before !== 0) return;
      queue.push(vertex);
      check[vertex] = true;
    });
  }

  // 모든 정점을 방문하기 전에 큐가 빈다면 사이클이 존재하는 것임.
  // 만약 선수 과목의 대상이 아닌 정점들은 false 로 표시될 것임. 하지만 선수 과목이 아니기 때문에 false 여도 상관없는 문제의 케이스도 고려함.
  // check [ true, true, true ] 모든 정점을 방문함
  return !check.some((c, k) => !c && hash[k]);
};

console.log(
  canFinish(1, []) === true,
  canFinish(2, [[1, 0]]) === true,
  canFinish(2, [[1, 0], [0, 1]]) === false,
  canFinish(3, [[0, 2], [1, 2], [2, 0]]) === false,
  canFinish(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]) === true,
  canFinish(3, [[1, 0], [2, 0], [0, 2]]) === false,
  canFinish(3, [[1, 0]]) === true,
  canFinish(3, [[1, 0], [2, 0]]) === true,
  canFinish(4, [[3, 0], [0, 1]]),
);
