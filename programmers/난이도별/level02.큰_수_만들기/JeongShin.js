function solution(number, k) {

    let deleteCount = 0
    let removeIdx

    while (deleteCount < k) {
        const len = number.length
        removeIdx = len - 1
        for (let i = 0; i < len - 1; i++) {
            if (number[i] < number[i + 1]) {
                removeIdx = i
                break
            }
        }
        deleteCount++
        number = number.replace(number[removeIdx], "")
    }

    return number
}

console.log(solution("4177252841", 4))