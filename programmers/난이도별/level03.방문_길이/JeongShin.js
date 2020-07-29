class player {
    constructor(x, y) {
        this.x = x;
        this.y = y;
        this.visited = {};
        this.count = 0;
    }

    getPos() {
        return this.x + ',' + this.y;
    }

    move(dir) {
        const currPos = this.getPos();

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

        this.checkOutOfBound();

        const nextPos = this.getPos();

        if (currPos === nextPos)
            return;

        const move = currPos + 'to' + nextPos;
        const opposite = nextPos + 'to' + currPos;

        if (!this.visited[move]) {
            this.visited[move] = true;
            this.visited[opposite] = true;
            this.count++;
        }
    }

    checkOutOfBound() {
        const [x, y] = [Math.abs(this.x), Math.abs(this.y)]
        if (x > 5) {
            this.x = this.x - Math.sign(this.x);
        }
        if (y > 5) {
            this.y = this.y - Math.sign(this.y);
        }
    }
}

function solution(dirs) {
    const p = new player(0, 0);
    for (const dir of dirs) {
        p.move(dir);
    }
    return p.count;
}