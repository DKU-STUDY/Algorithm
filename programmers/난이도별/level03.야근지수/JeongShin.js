class priorityQueue {
    constructor(arr) {
        this.queue = arr;
        this.queue.sort((a, b) => a - b);
        this.rear = arr.length;
    }

    push(el) {
        this.queue.push(el);
        this.queue.sort((a, b) => a - b);
        this.rear++;
    }

    pop() {
        const result = this.queue.pop();
        if (result) {
            this.rear--;
            return result;
        }
    }

    peek() {
        if (this.rear > 0)
            return this.queue[this.rear - 1];
        return 0;
    }
}

function solution(n, works) {
    const queue = new priorityQueue(works)
    while (n > 0) {
        const curr = queue.pop();
        n--
        queue.push(curr - 1);
    }
    return works.reduce((acc, curr) => acc + (curr > 0 ? curr ** 2 : 0), 0)
} 