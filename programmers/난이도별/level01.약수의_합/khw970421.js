function solution(n) {
    let sum=0;
    for(let i=1;i<=n;i++)
    {
        if(n%i==0) //나누어 떨어지면(약수이면)
            sum+=i //약수이므로 더해준다.
    }
    return sum;
}
