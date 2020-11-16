function solution(n, delivery) {
    let answer = new Array(n+1).fill(undefined);
    const needCheck = [];

    for (const [p1, p2, result] of delivery) {
        if (result) {
            answer[p1] = answer[p2] = "O";
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
        answer[p1] = answer[p1] || "?";
        answer[p2] = answer[p2] || "?";
    }
    return answer.slice(1).map((v)=> !v ? "?" : v).join("");
}

solution(6, [[1, 3, 1], [3, 5, 0], [5, 4, 0], [2, 5, 0]]);