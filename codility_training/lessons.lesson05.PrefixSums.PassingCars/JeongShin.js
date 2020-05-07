function solution(A) {
    let othercar = A.reduce((acc, curr) => {
        return curr !== A[0] ? acc + 1 : acc;
    }, 0);
    let cars = 0;
    A.forEach(el => {
        if (el === 0)
            cars += othercar;
        else
            othercar--;
    });
    return cars < 1000000001 ? cars : -1;
}