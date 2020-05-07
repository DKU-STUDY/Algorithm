function solution(A) {
    let othercar = A.reduce((acc, curr) => acc + (curr !== A[0]))
        return curr !== A[0] ? acc + 1 : acc;
    }, 0);
    let cars = 0;
    A.forEach(el => !el ? othercar-- : cars += othercar)
        if (el === 0)
            cars += othercar;
        else
            othercar--;
    });
    return cars < 1000000001 ? cars : -1;
}
