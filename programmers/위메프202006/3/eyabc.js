function solution (N, M, map) {
  var answer = '';
  let index

  const f = ([x, y], space) => {
    console.log(space)
    if (map[x][y] === "*") return space;
    space.push(map[x][y]);
    f([x+1, y], space)
    f([x, y+1], space)
  };


  console.log(f([0, 0], []));
}

console.log(solution(5, 7,
  ['--*AB**',
        'AB*A*BA',
        'B*-A*BB',
        '*-A*A**',
        'BC*BC*C']) === 'A5B5C1');

console.log(solution(9, 6, ['*****Z', '******', 'HH-I*A', '**IH*B', 'C*-***', 'C**---', 'CAZBBA', 'ZZ****', '***F**']) === 'A1B0C3F1H3I0Z1');
