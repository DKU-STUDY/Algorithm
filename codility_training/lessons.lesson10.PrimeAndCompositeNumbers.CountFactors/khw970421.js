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

