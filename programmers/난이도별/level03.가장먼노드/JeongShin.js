class queue {
    constructor() {
        this.queue = [];
        this.front = 0;
        this.rear = 0;
    }

    isEmpty() {
        return this.rear <= this.front;
    }

    push(v) {
        this.queue.push(v);
        this.rear++;
    }

    pop() {
        const result = this.queue[this.front];
        if (result) {
            this.front++;
            return result;
        }
    }
}

function solution(n, edge) {
    const graph = {};

    const bfs = (start) => {
        const Q = new queue();
        Q.push({vertex: start, distance: 0});

        const visited = {};
        visited[start] = 0;

        while (!Q.isEmpty()) {
            const {vertex, distance} = Q.pop();
            graph[vertex].forEach((neighbor) => {
                if (visited[neighbor] === undefined) {
                    visited[neighbor] = distance + 1;
                    Q.push({vertex: neighbor, distance: distance + 1});
                }
            });
        }
        return Object.values(visited);
    };

    for (const v of edge) {
        const [from, to] = v;
        graph[from] = (graph[from] || []);
        graph[to] = (graph[to] || []);
        graph[from].push(to);
        graph[to].push(from);
    }

    const distances = bfs(1);
    const max_distance = Math.max(...distances);

    return distances.reduce((count, distance) => count + (distance === max_distance), 0);
}

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]);
