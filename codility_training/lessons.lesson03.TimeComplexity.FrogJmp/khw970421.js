
function solution(X, Y, D) {
    return Math.ceil((Y - X) / D);            // 가려는 위치에 딱맞으면 올림없이 출력, 가려는 위치보가 더 필요하면 ceil로 인해 소수값 존재 올림
}
console.log(solution(10,85,30)===3);
console.log(solution(10,85,15)===5);


