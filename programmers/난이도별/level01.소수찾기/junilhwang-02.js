function solution(n) {
    const arr = []
    for (let i = 0; i < n; i++) arr.push(i+1)
    delete arr[0]
    const max = Math.pow(n, 1/2)
    for (let i = 2; i <= max; i++) {
        if (arr[i-1]) for (let j = i+i; j <= n; j += i) delete arr[j-1]
    }
    return arr.filter(v => v).length
}