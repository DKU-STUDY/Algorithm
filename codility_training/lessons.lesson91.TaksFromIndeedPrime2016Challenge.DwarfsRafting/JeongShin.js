/*
Assumption 에
each seat number can appear no more than once in the strings
이란 조건이 있는데 S, T 를 따로 놓고 봤을때 한번씩 나온다는 뜻이지 (S에서 "1B" 가 나오면 다시 안 나오지만 T에서 "1B"가 나올수 있음을 의미) S, T 에 중복으로 나오는 테스트 케이스가 있는거 같네요.
다른 분들 풀이 하실때 참고하시면 좋을꺼 같아요.
* */

function solution(N, S, T) {
    const getIdx = str => {
        const number = Array.from(str);
        const alphabet = number.pop();
        const [n, a] = [parseInt(number.join('')) - 1, alphabet.charCodeAt(0) - 65];
        return ~~(n / (N / 2)) * 2 + ~~(a / (N / 2));
    };

    const raft = new Array(4).fill((N / 2) ** 2);

    let count = 0;

    if (S.length)
        S.split(" ").forEach((str) => {
            raft[getIdx(str)]--;
        });

    let dwarfOnBoardCount = 0;

    if (T.length) {
        const dwarfOnBoard = T.split(" ");
        dwarfOnBoardCount = dwarfOnBoard.length;
        for (const str of dwarfOnBoard) {
            const curr = getIdx(str);
            const opposite = Math.abs(3 - curr);
            if ((--raft[curr] > -1) * (--raft[opposite] > -1) === 1)
                count += 2;
            else if (raft[curr] === -1 && raft[opposite] === -1)
                return 0;
            else return -1;
        }
    }

    return (Math.min(raft[0], raft[3]) + Math.min(raft[1], raft[2])) * 2 + count - dwarfOnBoardCount
}

