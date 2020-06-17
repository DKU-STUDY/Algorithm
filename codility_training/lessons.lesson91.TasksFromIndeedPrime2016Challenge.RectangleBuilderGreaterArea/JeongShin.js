/*
* 커밋 해두고 다시 풀어보겠습니다 ,,,
* */

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

    const len = temp2.length;
    let result = 0;
    for (let i = 0; i < bound; i++) {
        const curr = temp2[i];
        const target = Math.ceil(X / curr);
        let start = bound;
        let end = len - 1;
        let mid;
        // target 보다 같거나 큰 가장 작은 수의 index 를 binary search
        while (start <= end) {
            mid = ~~((start + end) / 2)
            if (target === temp2[mid])
                break;
            else if (target < temp2[mid])
                end = mid - 1;
            else
                start = mid + 1;
        }
        result = result + len - mid;
    }
    return result;
}


solution([1, 2, 5, 1, 1, 2, 3, 5, 1, 11], 5);