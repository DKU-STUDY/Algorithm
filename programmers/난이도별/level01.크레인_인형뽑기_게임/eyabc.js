// row 를 column 으로 바꿈
const transRow2Col = (arr, row) => {
    row.forEach((item, idx) => {
        if (!arr[idx])
            arr.push([]);
        arr[idx].push(item);
    });
};
// 행과 열을 바꾼다.
const newMachine = (board) => {
    return board.reduce((arr, row) => {
        transRow2Col(arr, row);
        return arr;
    }, []);
};

function solution (board, moves) {
    const machine = newMachine(board);

    return moves.reduce(({ basket, deleteCnt }, move) => {
        const pick = move - 1;

        // 해당 열에서 가장 먼저 나오는 인형을 pick 한다.
        machine[pick].find((dol, idx) => {
            const result = dol !== 0;
            // 해당 열에서 인형이 존재하면
            if (!result) return result;
            // 바구니 최상위의 인형과 동일한 종류일 때, deleteCnt 을 추가해 준다.
            if (basket[basket.length - 1] === dol) {
                deleteCnt += 2;
                machine[pick][idx] = 0;
                basket.pop();
                return true;
            }
            basket.push(dol);
            machine[pick][idx] = 0;
            
            
        });
        return { basket, deleteCnt };
    }, { basket: [], deleteCnt: 0 }).deleteCnt;
}

console.log(
    solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
        [1, 5, 3, 5, 1, 2, 1, 4]) === 4,
);
