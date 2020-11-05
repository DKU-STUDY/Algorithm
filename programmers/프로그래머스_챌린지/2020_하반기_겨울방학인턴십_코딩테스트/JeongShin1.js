function solution(n, delivery) {
    let answer = new Array(n+1).fill(undefined);
    const needCheck = [];

    for (const [p1, p2, result] of delivery) {
        if (result) {
            answer[p1] = "O";
            answer[p2] = "O";
            continue;
        }
        needCheck.push([p1, p2]);
    }

    for (const [p1, p2] of needCheck) {
        if (answer[p1]==="O"){
            answer[p2] = "X";
            continue;
        }
        if (answer[p2] === "O") {
            answer[p1] = "X";
            continue;
        }
        if (answer[p1] === undefined )
            answer[p1] = "?";
        if (answer[p2] === undefined)
            answer[p2] = "?";
    }
    answer = answer.map((v)=> !v ? "?" : v)
    answer.shift();
    return answer.join("")
}

solution(6, [[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]]);