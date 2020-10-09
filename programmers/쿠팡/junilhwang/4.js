function solution (depar, hub, dest, roads) {
  const graph = roads.reduce((path, [start, end]) => {
    path[start] = path[start] || [];
    path[start].push(end);
    return path;
  }, {});

  let result = 0;
  const f = (paths, last) => {
    if (last === dest) {
      console.log(paths);
      result += paths.includes(hub);
      return;
    }

    graph[last].forEach(v => {
      f(paths.concat([ v ]), v);
    });
  }

  f([ depar ], depar);

  return result;
}


console.log(
  solution(
    "SEOUL",
    "DAEGU",
    "YEOSU",
    [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
  ),
  9
);

console.log(
  solution(
    "ULSAN",
    "SEOUL",
    "BUSAN",
    [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
  ),
  0
);