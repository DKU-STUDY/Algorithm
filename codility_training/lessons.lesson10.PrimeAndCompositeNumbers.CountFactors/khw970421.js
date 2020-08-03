//정확성 효율성 100
function solution(N)
{
    let cnt = 0;
    for(let i = 1; ; i++)
    {
        if(i>=Math.sqrt(N)){  //제곱근 전까지만 반복(만약 많이 커져도 갈수록 제곱근은 크게 늘어나는것이 아니기때문에 반복이 그나마 적다
            break;
        }
        if (N % i == 0) {     //제곱근 전까지의 약수의 갯수 구하기
            cnt++; // 약수 개수
            // i 약수
        }
    }
    cnt*=2;        // 제곱근 전과 후에 곱해야 원래 값이나오므로 2배하기
    let q=Math.sqrt(N);    //제곱근값 대입
    if(Number.isInteger(q))     //제곱근 값이 만약 정수라면 그갯수도 포함해 더한다( 자신을 제곱하면 원래값이 되므로 ex) 5*5==25 , 4.321*4.321 != 24이므로)
        cnt++;
    return cnt;   //합친값을 return
}

//피드백 후 코드

function solution1(N)
{
    let cnt = 0;
    const q = Math.sqrt(N);
    for(let i = 1; i < q ;i++)
        cnt += N % i == 0;      //제곱근까지 돌리면서 약수의 갯수를 구하기 N%i==0이면 결국 1이니 cnt=cnt+1이 되므로 약수희 갯수 증가
    return cnt*2 + Number.isInteger(q); //제곱근 전까지의 값을 2배하고 제곱근이 정수인 값이라면 그 값도 더해야 하기때문에 1을 더한다.
                                        // (Number.isInteger는 T/F 받으므로 T이면 더했을때 1로 처리되서 더하기 때문에 가능
}

