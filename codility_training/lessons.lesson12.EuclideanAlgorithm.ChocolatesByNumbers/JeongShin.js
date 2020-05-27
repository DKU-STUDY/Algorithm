function solution(N, M) {
    let count = 1;
    let curr = M;
    while (curr % N !== 0) {
        curr = (curr += M) % N
        count++;
    }
    return count;
}