function solution(n)
{
    let a=[],sum=0;
    a.push(String(n));  //숫자를 문자로 바꿔서 a배열에 넣는다.

    a[0].split('').forEach(function(e){     //넣은것을 글자마다 분리하여 그때의 숫자를 더하여 계산
        sum+=Number(e);
    })
    return sum;
}
