function solution(A) {
    let othercar = A.reduce((acc, curr) => acc + (curr !== A[0]));
    let cars = 0;
    A.forEach(el => !el ? othercar-- : cars += othercar);
    return cars < 1000000001 ? cars : -1;
}
