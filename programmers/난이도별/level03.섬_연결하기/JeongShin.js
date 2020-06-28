
function solution(n, costs) {
    // set 은 각 노드별로 자신의 부모를 가르킵니다. 음수는 부모가 자기 자신임을 의미하고 중치는 자식의 개수를 의미 합니다.
    const set = new Set();

    // 그리디 알고리즘을 사용하기 위해 weight 순으로 정렬 (이후에 pop 을 사용 하기 때문에 내림차순 정렬)
    const sorted_costs = costs.sort((a, b) => (b[2] - a[2]));

    const find = (set, child) => {
        let parent = child;
        while (set[parent] >= 0) {
            parent = set[parent]
        }
        return parent;
    };

    const union = (set, p1, p2) => {
        const [parent, child] = [set[p1] < set[p2] ? p1 : p2, set[p1] < set[p2] ? p2 : p1];
        set[parent] = set[p1] + set[p2];
        set[child] = parent;
    };

    // Array 를 이용해도 되지만 node 의 index 가 0,1,2 ... 순차적으로 오는게 아닐 경우 Set 이 적합하다 생각합니다.

    sorted_costs.forEach(el => {
        set[el[0]] = -1;
        set[el[1]] = -1;
    });

    let ans = 0;

    /* Union - Find */
    while (sorted_costs.length) {
        const [node1, node2, weight] = sorted_costs.pop();

        // Find parents of each nodes
        const par1 = find(set, node1);
        const par2 = find(set, node2);

        // Same parent 👉 Cycle exists 👉 Skip
        if (par1 === par2)
            continue;

        // Union two sets
        union(set, par1, par2);

        // Add weight to answer
        ans += weight;

    }

    return ans;
}

solution(5, [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]]);
