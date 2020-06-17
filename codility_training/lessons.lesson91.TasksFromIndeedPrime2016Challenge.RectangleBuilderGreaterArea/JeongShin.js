function solution(A, X) {
    const temp = A.reduce((arr, val) => {
        arr[val] = (arr[val] || 0) + 1;
        return arr;
    }, {});
    const temp2 = [];
    for (const [key, val] of Object.entries(temp)) {
        if (val >= 2)
            temp2.push(parseInt(key));
    }

    const bound = ~~Math.sqrt(X);
    const [small, big] = temp2.reduce(([small, big], curr) => {
        if (curr <= bound)
            small.push(curr);
        else
            big.push(curr);
        return [small, big];
    }, [[], []]);


// return result > 1000000000 ? -1 : result;

}

//
// const pieces = temp.reduceRight(([arr, acc], curr, idx) => {
//     if (curr >= 2) acc++;
//     arr[idx] = acc;
//     return [arr, acc]
// }, [[], 0])[0]
//
// let result = 0;
//
// for (let x = 1; x <= ~~(X / 2); x++) {
//     const y = Math.ceil(X / x);
//     if (pieces[y])
//         result += pieces[y];
// }
//


solution([1, 2, 5, 1, 1, 2, 3, 5, 1, 11], 5);