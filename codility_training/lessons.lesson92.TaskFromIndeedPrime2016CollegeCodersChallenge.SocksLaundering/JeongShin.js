/*
* Solution 1 👉 Correctness 90%
* 1.544 sRUNTIME ERROR, tested program terminated with exit code 134
* stderr:
* terminate called after throwing an instance of 'std::bad_alloc'
* what():  std::bad_alloc
*
* 모든 노드들 마다 socks 오브젝트가 복사 되어서 만들어지기 때문에 메모리를 너무 많이 할당해서
* 문제가 생기는거라 생각되는데 어떻게 해결해야할지 모르겠네요 ㅠ ㅠ
* */

function solution(K, C, D) {
    class node {
        constructor(c, k, s) {
            this.c = c;
            this.k = k;
            this.s = s;
        }
    }

    const socks = {};
    let clean_socks = 0;

    for (const val of C) {
        socks[val] = (socks[val] || 0) + 1;
        if (socks[val] === 2) {
            clean_socks++;
            socks[val] = 0;
        }
    }

    let stack = [new node(0, K, socks)];
    const result = [];

    for (const val of D) {
        const next = [];
        while (stack.length) {
            const curr = stack.pop();
            // val 을 포함 하는 경우
            const temp = {...curr.s};
            const new_pair = temp[val] === 1;
            temp[val] = (!new_pair) * 1;
            if (curr.k > 0)
                next.push(new node(curr.c + new_pair, curr.k - 1, temp));
            else
                result.push(curr.c);
            // val 을 포함 안하는 경우
            next.push(curr);
        }
        stack = next;
    }

    stack.forEach((val) => {
        result.push(val.c)
    });

    return clean_socks + (result.length ? Math.max(...result) : 0);
}

solution(2, [1, 2, 1, 1], [1, 4, 3, 2, 4]);
