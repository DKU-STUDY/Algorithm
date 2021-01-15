const parseToArr = (s) => JSON.parse(s.replace(/{/gi, '[').replace(/}/gi, ']'));
const sortByLength = (a, b) => a.length - b.length;
const getOrigin = (origin, tuple) => {
    origin.push(tuple.filter(num => !origin.includes(num))[0]);
    return origin;
};

function solution (s) {
    return parseToArr(...arguments)
        .sort(sortByLength)
        .reduce(getOrigin, []);
}

console.log(
    solution('{{2},{2,1},{2,1,3},{2,1,3,4}}') === [2, 1, 3, 4],
    solution('{{1,2,3},{2,1},{1,2,4,3},{2}}') === [2, 1, 3, 4],
    solution('{{20,111},{111}}') === [111, 20],
    solution('{{123}}') === [123],
    solution('{{4,2,3},{3},{2,3,4,1},{2,3}}') === [3, 2, 4, 1],
);