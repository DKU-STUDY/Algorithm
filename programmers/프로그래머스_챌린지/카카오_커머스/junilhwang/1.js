function solution(n, record) {
  return record.reduce((serverMap, v) => {
    const [serverKey, nickName] = v.split(' ');
    const server = serverMap[serverKey] || [];
    if (server.includes(nickName)) return serverMap;
    server.push(nickName);
    serverMap[serverKey] = server.slice(-5);
    return serverMap;
  }, []).flatMap(server => server);
}

console.log(
  solution(1, ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"]),
  solution(4, ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]),
)
