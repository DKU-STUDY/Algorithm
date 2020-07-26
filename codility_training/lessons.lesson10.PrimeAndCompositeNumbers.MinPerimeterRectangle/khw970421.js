//정확성 효율성 100
function solution(N)
{
    let count=0;
    let num=[];

    let q=Math.sqrt(N);
    if(Number.isInteger(q))  //약수가 홀수개일때 가장 작은 값은 루트한 값을 4배한것
        return 4*q;

    for(let i=1; i<=Math.sqrt(N); i++) //약수가 짝수개일때 루트값 전까지 약수를 구한다
    {
        if(N % i == 0)
        {
            count++;
            num.push(i);
        }
    }

    const l=num.length;
    let k = N/num[l-1];      //가장 마지막 값은 N의 약수의 중간값이기 때문에 그다음 값 k를구한다. ex) 8=40/5
    return 2*(k+num[l-1]);   //두개를 더하고 곱한값을 return
}

//수정본
function solution1(N)
{
    const num=[];
    const q=Math.sqrt(N);

    if(Number.isInteger(q))  //약수가 홀수개일때 가장 작은 값은 루트한 값을 4배한것
        return 4*q;

    for(let i=1; i<=q; i++) //약수가 짝수개일때 루트값 전까지 약수를 구한다
        if(N % i == 0)
            num.push(i);

    const l=num.pop();
    const k = N/l;      //가장 마지막 값은 N의 약수의 중간값이기 때문에 그다음 값 k를구한다. ex) 8=40/5
    return 2*(k+l);   //두개를 더하고 곱한값을 return
}