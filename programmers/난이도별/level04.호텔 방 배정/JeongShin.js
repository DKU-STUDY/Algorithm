function solution(k, room_number) {
    const room = new Map();

    const findAndUnion = (n) => {
        // find
        if (!room.has(n)) {
            room.set(n, n + 1);
            return n;
        }
        let parent = findAndUnion(room.get(n));
        // union
        room.set(n, parent + 1);
        return parent;
    };

    return room_number.reduce((answer, roomRequest) => {
        answer.push(findAndUnion(roomRequest));
        return answer;
    }, [])
}

/* 효율성 테스트 케이스 3개 불합격 */
function solution2(k, room_number) {
    const room = {};

    const findAndUnion = n => {
        let curr = room[n], prev;
        while (curr.using) {
            prev = curr;
            curr = room[curr.parent];
            prev.parent = curr.parent;
        }
        // prev.forEach((v)=> room[v].parent = curr.parent);
        return curr.idx;
    };

    // 여기서 모든 방에 대해서 부모를 설정할 필요가 없음.
    for (let i = 1; i <= k; i++) {
        room[i] = {idx : i, using: false, parent: i + 1};
    }

    return room_number.map((n)=>{
        if (room[n].using)
            n = findAndUnion(n);
        room[n].using = true;
        return n;
    })
}


console.log(solution(10, [1, 3, 4, 1, 3, 1]));