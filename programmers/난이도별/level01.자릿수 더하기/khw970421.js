function solution(n)
{
    let sum=0;


    String(n).split('').forEach(function(e){     //넣은것을 글자마다 분리하여 그때의 숫자를 더하여 계산
        sum+=Number(e);
    })
    return sum;
}


//내가 새로수정한 코드
function solution(n)
{
    let sum=0;
    return  String(n).split('').map(e=>sum+=Number(e)).pop()

}

//피드백 받은 코드
function solution(n)
{
    return String(n).split('').map(Number).reduce((a, b) => a + b);
}
