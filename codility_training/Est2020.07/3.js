function diff (maps, x, y, r, range) {
    let cnt = 0;
    const h = r / 2;
    for (let i = 0 ; i < r ; i++) {
        const Y = x + i - h;
        if (!maps[Y]) continue;
        for (let j = 0 ; j < r ; j++) {
            const X = y + j - h;
            if (!maps[Y][X]) continue;
            if (maps[Y][X] <= range[i][j]) {
                cnt += 1;
            }
        }
    }
    return cnt;
}

const makeRange = (r) => {
    const range = new Array(r);
    for (let i = 0 ; i < r ; i++) {
        range[i] = new Array(r).fill(0);
    }
    return range;
};

function solution (maps, p, r) {
    const range = makeRange(r);
    const h = r / 2;

    // 공격 데미지 범위를 나타내는 배열
    for (let i = 0 ; i < h ; i++) {
        range[i][h - i - 1] = p / 2;
        range[i][h + i] = p / 2;
        range[h + i][i] = p / 2;
        range[h + i][r - i - 1] = p / 2;

        for (let j = h - i ; j < h + i ; j++) {
            range[i][j] = p;
        }
        for (let j = i + 1 ; j < r - i - 1 ; j++) {
            range[h + i][j] = p;
        }
    }

    let max = 0;
    const mapsLen = maps.length;
    for (let i = 0 ; i < mapsLen ; i++) {
        for (let j = 0 ; j < mapsLen ; j++) {
            max = Math.max(diff(maps, i, j, r, range), max);
        }
    }
    return max;
}

console.log(
    solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29], [39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]], 19, 6) === 17,
    // solution([[47, 8, 99, 9, 85, 3, 8], [90, 93, 8, 25, 98, 15, 97], [9, 95, 91, 87, 8, 81, 9], [98, 88, 82, 89, 79, 81, 97], [97, 35, 31, 97, 81, 2, 92], [32, 16, 49, 9, 91, 89, 17], [53, 6, 35, 12, 13, 98, 5]], 78, 6) === 11,
    // solution([[9, 8, 17, 55, 19, 7], [1, 25, 5, 39, 28, 8], [88, 19, 28, 3, 2, 9], [76, 73, 7, 18, 16, 14], [99, 8, 8, 7, 11, 9], [1, 18, 4, 10, 3, 6]], 16, 4) === 8,
    // solution([[6, 3, 2, 7, 3], [7, 2, 1, 6, 8], [8, 9, 8, 4, 9], [7, 9, 2, 7, 1], [6, 3, 6, 8, 4]], 5, 2) === 3,
);


// r 은 짝수
// 블루는 r * 2
// 옐로는 Y(n-1) + B(n - 1)
// 공격범위 좌표: