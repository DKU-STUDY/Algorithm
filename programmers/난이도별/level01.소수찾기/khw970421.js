//처음 생성한 코드 (효율성 및 큰 n에따라 런타임아웃)

function solution(n) {
    let k=[],count=0;
    for(let i=2;i<=n;i++)
    {    count=0;
        for(let j=2;j<i;j++)
        {
            if(i%j!=0)
            {  count++;
            }
        }
        if(count+1==i-1)
            k.push(i);
    }
    return k.length;
}

// 다른 사람의 코드 확인

function solution(n) {
    const s = new Set();
    for(let i=1; i<=n; i+=2){
        s.add(i);
    }
    s.delete(1);
    s.add(2);
    for(let j=3; j<Math.sqrt(n); j++){
        if(s.has(j)){
            for(let k=j*2; k<=n; k+=j){
                s.delete(k);
            }
        }
    }
    return s.size;
}

//다른사람 코드를 확인후 수정
function solution(n) {
    const s = new Set();
    for(let i=1; i<=n; i+=2){
        s.add(i);
    }
    s.delete(1);
    s.add(2);   // n보다 작거나 같은 개수중 짝수2와 1을제외한 나머지 홀수들을 s에 넣는다.

    for(let j=3; j<Math.sqrt(n); j++){     // 3부터 n의 루트의 크기까지 반복한다.
        if(s.has(j)){                       // 맞는 값이 있다면
            for(let k=j*2+j; k<=n; k=k+2*j){    // n보다 작은 자신의 원래값보다 배수에 만족하는 홀수들을 전부 없앤다
                s.delete(k);
            }
        }
    }
    return s.size;
}
/*실질적으로 j=3일때 k가 6이되는 k를 없애는데 실제 s에는 짝수는 2밖에없으므로 코드낭비라 생각하므로
let k = j*2+j로 만들어 없애고 이를 반복하는 것은 자신의 원래크기에 2*j를 더한수를 반복해야 홀수를 계속 찾아 삭제한다 생각

추가적으로 효울적인 이유가 Math.sqrt(n)을 통해 밖의 for문이 엄청 적게 돌아가기때문이다. (저렇게해도 되는게 뭔가신기하다)
 */
