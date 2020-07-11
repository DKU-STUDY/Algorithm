class minMaxHeap {
    constructor() {
        this.queue = [];
        this.rear = 0;
    }

    push(el) {
        this.queue.push(el);
        this.rear++;
        this.queue.sort((a, b) => b - a);
    }

    popMin() {
        if (this.rear > 0) {
            this.rear--;
            return this.queue.pop();
        }
        return 0;
    }

    popMax() {
        if (this.rear > 0) {
            this.rear--;
            return this.queue.shift();
        }
        return 0;
    }
}

function solution(operations) {
    const heap = new minMaxHeap();
    for (const o of operations) {
        const [command, data] = o.split(" ");
        if (command === 'I')
            heap.push(data * 1);
        else {
            data === '1' ? heap.popMax() : heap.popMin();
        }
    }
    return [heap.popMax(), heap.popMin()];
}

console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))