
function solution(X, Y, D) {
    if((Y-X)%D==0)                                   //크기에 맞게 딱 나눠 위치까지 도달하면
        return Math.floor((Y-X)/D);               // 가려는 위치에서 원래 위치를 뺀후 크기만큼 나눈후만큼 return
    else                                             //크기보다 더 부족하면
        return Math.floor((Y-X)/D+1);               // 한칸 더 옮겨야하므로 1이 추가
}

console.log(solution(10,85,30)===3);
console.log(solution(10,85,15)===5);


