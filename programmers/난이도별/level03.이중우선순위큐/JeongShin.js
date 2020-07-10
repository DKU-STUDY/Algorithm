
/*
* 풀이 진행중 ,,, 
* */

class queue {
    constructor() {
        this.queue = [];
        this.rear = 0;
    }

    push(element) {
        this.queue.push(element);
        this.rear++;
        this.bubbleUp();
    }

    pop() {
        const result = this.queue[0];
        const end = this.queue.pop();
        this.rear--;
        if (this.rear > 0) {
            this.queue[0] = end;
            this.bubbleDown();
        }
        return result;
    }

    bubbleDown() {
        let idx = 0;
        const length = this.queue.length;
        const element = this.queue[0];
        while (true) {
            let leftChildIdx = 2 * idx + 1;
            let rightChildIdx = 2 * idx + 2;
            let leftChild, rightChild;
            let swapIdx = null;
            if (leftChildIdx < length) {
                leftChild = this.queue[leftChildIdx];
                if (this.compare( element,leftChild)) {
                    swapIdx = leftChildIdx;
                }
            }
            if (rightChildIdx < length) {
                rightChild = this.queue[rightChildIdx];
                if (
                    (swapIdx === null && this.compare(element, rightChild)) ||
                    (swapIdx !== null && this.compare(leftChild, rightChild))
                )
                    swapIdx = rightChildIdx;
            }
            if (swapIdx === null)
                break;
            this.queue[idx] = this.queue[swapIdx];
            this.queue[swapIdx] = element;
        }
    }

    bubbleUp() {
        let idx = this.rear - 1;
        const element = this.queue[idx];
        while (idx > 0) {
            let parentIdx = ~~((idx - 1) / 2);
            let parent = this.queue[parentIdx];
            if (this.compare(element, parent))
                break;
            else {
                this.queue[parentIdx] = element;
                this.queue[idx] = parent;
                idx = parentIdx;
            }
        }
    }

    compare(a, b) {
    }

}

class minQueue extends queue {
    compare(a, b) {
        return a > b;
    }
}

class maxQueue extends queue {
    compare(a, b) {
        return a < b;
    }
}

const max = new maxQueue()
const min = new minQueue()



// const op = ["I 16", "D 1"];
// solution(op);
// operations.forEach((el) => {
//     const [operation, option] = el.split(" ");
// })