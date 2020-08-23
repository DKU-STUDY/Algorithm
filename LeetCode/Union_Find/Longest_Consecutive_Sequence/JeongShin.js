/*
* [100, 4, 200, 1, 3, 2] 와 같이 배열이 있을때
* 가장 긴 연속된 숫자의 길이를 반환 하는 문제
* 따라서 [1, 2, 3, 4] 의 연속된 숫자가 존재하기 때문에 4를 반환 해야함.
* */

/* 나의 풀이 */
class Node {
    constructor(end, parent, children) {
        this.end = end;
        this.parent = parent;
        this.children = children;
    }
}

const longestConsecutive = function (nums) {
    const map = new Map();

    const find = (num) => {
        let parent = num;
        while (!map.get(parent).end)
            parent = map.get(parent).parent;
        return parent;
    };

    const union = (p1, p2) => {
        const [c1, c2] = [map.get(p1).children, map.get(p2).children];
        const [parent, child] = c1 > c2 ? [p2, p1] : [p1, p2];
        map.set(parent, new Node(true, null, c1 + c2));
        map.set(child, new Node(false, parent, 0));
    };

    for (const num of nums) {
        const [left, right] = [num - 1, num + 1];

        if (map.has(num))
            continue;
        map.set(num, new Node(true, null, 1));

        if (map.has(left))
            union(...[num, left].map(find));
        if (map.has(right))
            union(...[num, right].map(find));
    }

    let answer = 0;

    for (const [k, v] of map)
        answer = Math.max(v.children, answer);

    return answer;
};

longestConsecutive([100, 4, 200, 1, 3, 2]);

/* 다른 사람 코드를 참고한 풀이 */

const longestConsecutive2 = function (nums) {
    const map = new Map();
    let answer = 0;
    for (const num of nums) {
        if (map.has(num))
            continue;
        let left = map.has(num - 1) ? map.get(num - 1) : 0;
        let right = map.has(num + 1) ? map.get(num + 1) : 0;
        let sum = left + right + 1;
        map.set(num, sum);

        answer = Math.max(sum, answer);

        map.set(num - left, sum);
        map.set(num + right, sum);
    }
    return answer;
};

longestConsecutive2([100, 4, 200, 1, 3, 2]);


