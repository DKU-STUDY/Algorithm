// dp 를 이용한 풀이
function solution(sticker) {
    const len = sticker.length;
    if (len < 3)
        return Math.max(...sticker);
    /* 첫번째 스티커를 뜯는 경우 */
    const dp1 = [sticker[0], sticker[0]];
    /* 첫번째 스티커를 뜯지 않는 경우 */
    const dp2 = [0, sticker[1]];

    let i;
    for (i = 2; i < len - 1; i++) {
        dp1[i] = Math.max(dp1[i - 2] + sticker[i], dp1[i - 1]);
        dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);
    }
    // 마지막 스티커 처리
    dp1[i] = Math.max(dp1[i - 1], dp1[i - 2]);
    dp2[i] = Math.max(dp2[i - 2] + sticker[i], dp2[i - 1]);

    return Math.max(dp1[i], dp2[i]);
}


solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([1, 3, 2, 5, 4])


// 1) 분기와 한정
// branch and bound 풀이로 접근하면 bound 없이는 정확한 답은 구할 수 있음.
// 하지만 2 ^ n 개의 노드를 생성하기 때문에 시간 복잡도가 극악이 됨.
// bound 하는 과정에서 마음대로 bound 를 하게 되면 원하지 않는 노드를 삭제하게 되는 문제가 생김.
// 👉 다른 풀이로 접근 필요
class Node {
    constructor(w, p, f) {
        this.weight = w;
        this.possible = p;
        this.firstNodeUsed = f;
    }
}

function solution2(sticker) {
    const len = sticker.length;
    let stack = [], next = [], bound = 0;

    // Case 1. 첫번째 노드를 미사용
    stack.push(new Node(0, true, false));
    // Case 2. 첫째째 노드 사용
    stack.push(new Node(sticker[0], false, true));

    for (let i = 1; i < (len - 1); i++) {
        while (stack[0]) {
            const node = stack.pop();

            if ((node.weight + sticker[i]) <= bound)
                continue;

            if (node.possible) {
                bound = node.weight;
                next.push(new Node(node.weight + sticker[i], false, node.firstNodeUsed));
            }

            node.possible = true;
            next.push(node);
        }
        stack = next;
        next = [];
    }


    // 마지막 노드는 첫번째 노드 사용 여부에 따라 따로 처리 해준다.
    return stack.reduce((answer, currNode) => {
        if (!currNode.firstNodeUsed && currNode.possible)
            currNode.weight += sticker[len - 1];
        return Math.max(currNode.weight, answer);
    }, 0);
}

// solution([14, 6, 5, 11, 3, 9, 2, 10])
// solution([1, 3, 2, 5, 4])