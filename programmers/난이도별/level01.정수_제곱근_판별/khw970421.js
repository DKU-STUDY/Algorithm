function solution(n) {
    return (Number.isInteger(n**0.5))? (n ** 0.5 + 1) ** 2 : -1;
}
//sqrt한 값이 Integer인지 판단하고 맞으면 +1하고 제곱하고 아니면 -1리턴
