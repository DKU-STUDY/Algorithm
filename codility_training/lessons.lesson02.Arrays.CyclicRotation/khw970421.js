//방법1
function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)4
    const b=[];
    let size=A.length;
    for(let i=0;i<size;i++)
    {
        b[(i+K)%size]=A[i]; //b라는 곳에 자신의 값에 K만큼 옮긴것을 더한것에서 크기만큼 나눠준곳에 대입
    }
    return b;
}
//방법2
function solution1(A, K) {
    const shift = K%A.length;      //움직인 횟수 shift K의값이 크기보다 클경우 반복되는 횟수 나머지만 계산

    for(let i=0;i<shift;i++)                        //shift횟수만큼 반복
    {
        A.unshift(A[size-1]);                       //뒤의 값을 맨앞에 삽입
        A.pop();                                    //맨뒤의 값을 삭제
    }
    return A;
}

//방법3
function solution2(A, K) {
    const change = K%A.length;
    let reduced = A.splice(-change);     //뒤에서부터 크기만큼 start세우고 그만큼의 갯수를 reduced에 빼온다.

    return reduced.concat(A);
}

//방법4
function solution3(A, K) {
    const change = K%A.length;

    return [...A.splice(-change),...A];
}

console.log(solution1([3,8,9,7,6],3).toString()===[9,7,6,3,8].toString());
console.log(solution1([0,0,0],1).toString()===[0,0,0].toString());
console.log(solution1([1,2,3,4],4).toString()===[1,2,3,4].toString());
