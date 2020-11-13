function solution(number, k) {
    const stack = []
    const len = number.length
    let top = 0
    let deleteCount = 0

    for (let i = 0; i < len; i++) {
        const curr = number[i]
        if (top === 0) {
            stack.push(curr)
            top++
            continue
        }
        while (top > 0 && stack[top - 1] < curr) {
            stack.pop()
            deleteCount++
            top--;
            if (top === 0)
                break
            if (deleteCount === k)
                return stack.join('') + number.slice(i, len)
        }
        stack.push(curr)
        top++
    }
    return stack.join('').slice(0, len - k)
}

console.log(solution("4177252841", 4))

