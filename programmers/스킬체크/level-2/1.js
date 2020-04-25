function solution(s) {
    const arr = Array.from(s)
    const obj = {}
    arr.forEach(v => obj[v] = obj[v] ? obj[v] + 1 : 1)
    if (Object.values(obj).find(v => v % 2 !== 0)) return 0
    
    let chk = 0
    for (let i = 0, len = arr.length, x = 0, y = 1; i < len; i++) {
        if (x >= 0 && y < len && arr[x] === arr[y]) {
            arr[x--] = arr[y++] = null
            while(arr[x] === null) x--
            while(arr[y] === null) y++
            chk += 2
        } else {
            x = y++
        }
    }
    return arr.length === chk ? 1 : 0;
}
console.log(solution("baabaa"))
console.log(solution("cdcd"))