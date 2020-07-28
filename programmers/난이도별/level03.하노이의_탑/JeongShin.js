/*
* | A | B | C |
* Move n - 1 from A to B using C
* Move 1 from A to C
* Move n - 1 from B to C using A
* */

function solution(n) {
    const answer = [];

    const move = (n, A, B, C) => {
        if (n > 0) {
            move(n - 1, A, C, B)
            answer.push([A, C]);
            move(n - 1, B, A, C)
        }
    }
    move(n, 1, 2, 3)
    return answer;
}

// console.log(solution(3))

