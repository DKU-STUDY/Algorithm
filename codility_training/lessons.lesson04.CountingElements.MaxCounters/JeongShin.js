function solution(N, A) {
    if (!A || N === 0) return;
    const arr = new Array(N+1).fill(0);
    for (const val of A){
        if (val===N+1){
            arr.fill(arr[0]);
        }
        else {
            if (arr[0]<++arr[val])
                arr[0]=arr[val];
        }
    }
    return arr.slice(1);
}
solution(5, [3,4,4,6,1,4,4]);
