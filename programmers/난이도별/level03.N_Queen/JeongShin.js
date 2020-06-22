/*
* FIFO 방식 & 분기 한정을 이용한 구현
* Variables : n, col, level
*
* n 👉 board 의 크기
*
* col 👉 board 에 queen 의 위치
* col [1, 2] = | Q |   |
*              |   | Q |
*
* level 👉 현재 고려하고 있는 level 번째 queen
*
* queue 👉 각 노드별 level, col 의 순서대로 저장하기 위한 자료 구조
* | 2 | 1 | 2 |
* | level | col |
*
* 2 레벨 col [1, 2]를 저장
* */

class queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }

    push(el) {
        this.queue[this.rear++] = el;
    }

    pop() {
        if (this.front < this.rear) {
            return this.queue[this.front++];
        }
    }

    isEmpty() {
        return this.front === this.rear;
    }
}

function solution(n) {
    const Q = new queue();
    const col = [];
    let result = 0;
    let level = 0;
    Q.push(level);
    while (!Q.isEmpty()) {
        // pop current level & current col
        let level = Q.pop();
        for (let idx = 1; idx <= level; idx++)
            col[idx] = Q.pop();

        // next level
        level++;

        // branch creating each child node & bound through promising function
        for (let i = 1; i <= n; i++) {
            col[level] = i;
            // if node is alive
            if (promising(col, level)) {
                if (level === n)
                    result++;
                else {
                    Q.push(level); // push next level to queue
                    for (let idx = 1; idx <= level; idx++)
                        Q.push(col[idx]); // push current board to queue
                }
            }
            // else { node is dead 👉 don't push }
        }
    }
    return result
}

/*
* 현재 col 이 현재 level 까지 살아있는지 죽어있는지 판단 합니다.
* 판단 조건은
* 1. 퀸이 같은 line에 있을 경우
* 2. 퀸이 대각선에 있을 경우
* 죽은 노드가 됩니다. 즉 false 를 반환
* */
function promising(col, level) {
    let idx = 1;
    let isLive = true;
    while (idx < level && isLive) {
        // If Queens are in same line || diagonal 👉 node is dead
        isLive = !(col[idx] === col[level] || Math.abs(col[level] - col[idx]) === level - idx);
        idx++;
    }
    return isLive;
}

solution(4);