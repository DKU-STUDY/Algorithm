class minMaxHeap {
    constructor() {
        this.queue = [];
    }

    push(el) {
        this.queue.push(el);
        this.queue.sort((a, b) => b - a);
    }

    popMin() {
        const result = this.queue.pop();
        if (result){
            return result;
        }
        return 0;
    }

    popMax() {
        const result = this.queue.splice(0,1) * 1;
        if (result){
           return result
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
