function solution(arr, K) {
    if (arr && arr.length > 1) {
        for(let i = 0 ; i<K; i++) arr.unshift(arr.pop());
    }
    return arr;
}

function solution2 (arr, K) {
    if (K === 0 || K === arr.length) {
        return arr;
    }
    const t = K % arr.length;
    const index = arr.length - t;
    return [...arr.slice(index), ...arr.slice(0, index)];
}
