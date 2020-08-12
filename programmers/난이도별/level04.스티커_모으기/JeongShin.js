class Node {
    constructor(w, p, f) {
        this.weight = w;
        this.possible = p;
        this.firstNodeUsed = f;
    }
}

function solution(sticker) {
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