function solution(n) {
    const arr = [0]
    let len = 1
    let i = 1

    while (i < n) {
        for (let j = 1; j <= len; j++)
            arr[len + j] = 1 ^ arr[len - j]
        arr[len] = 0;
        len = len * 2 + 1
        i++
    }

    return arr
}

solution(3)