// function solution(number, k) {
//
//     let deleteCount = 0
//     let removeIdx
//
//     while (deleteCount < k) {
//         const len = number.length
//         removeIdx = len - 1
//         for (let i = 0; i < len - 1; i++) {
//             if (number[i] < number[i + 1]) {
//                 removeIdx = i
//                 break
//             }
//         }
//         deleteCount++
//         number = number.replace(number[removeIdx], "")
//     }
//
//     return number
// }
//
// console.log(solution("4177252841", 4))

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

