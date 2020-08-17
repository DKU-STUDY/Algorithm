class player {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.visited = {};
        this.count = 0;
    }

    currPos() {
        return this.x + ',' + this.y;
    }

    getNewPos(dir) {
        switch (dir) {
            case 'U':
                this.y++;
                break;
            case 'D':
                this.y--;
                break;
            case 'L':
                this.x--;
                break;
            case 'R':
                this.x++;
        }
    }

    move(dir) {
        const currPos = this.currPos();

        this.getNewPos(dir);

        this.checkOutOfBound();

        const nextPos = this.currPos();

        if (currPos === nextPos)
            return;

        const move = currPos + 'to' + nextPos;

        if (!this.visited[move]) {
            this.visited[move] = true;
            this.visited[nextPos + 'to' + currPos] = true;
            this.count++;
        }
    }

    checkOutOfBound() {
        const {x, y} = this;
        this.x -= (Math.sign(x) * (Math.abs(x) > 5))
        this.y -= (Math.sign(y) * (Math.abs(y) > 5))
    }
}

function solution(dirs) {
    const p = new player(0, 0);
    for (const dir of dirs)
        p.move(dir);
    return p.count;
}