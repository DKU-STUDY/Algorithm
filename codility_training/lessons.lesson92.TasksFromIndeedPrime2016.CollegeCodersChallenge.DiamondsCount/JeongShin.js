function solution(X, Y) {

}

// const getBound = arr => {
//     return arr.reduce(([min, max], curr) => {
//         return [Math.min(min, curr), Math.max(max, curr)];
//     }, [Infinity, 0])
// };
// const getCoords = arr => {
//     return arr.reduce((obj, curr) => {
//         obj[curr] = (obj[curr] || 0) + 1;
//         return obj;
//     }, {})
// };
// const [x_min, x_max] = getBound(X);
// const [y_min, y_max] = getBound(Y);
// const x_coords = getCoords(X);
// const y_coords = getCoords(Y);
// console.log(x_coords);
// console.log(y_coords);

solution([1, 1, 2, 2, 2, 3, 3], [3, 4, 1, 3, 5, 3, 4])