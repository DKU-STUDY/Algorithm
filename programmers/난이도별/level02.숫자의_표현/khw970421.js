function solution(n) {
    let answer=0;
    let count=0;
    for(let i=1;i<=n;i++)
    {
        answer=0;
        for(let j=i;j<=n;j++)
        {
            answer+=j;      // i부터 하나씩 계속 더하기
            if(answer==n){      //값이 같아지면 count 증가와 break
                count++;
                break;
            }
            else if(answer>n){  //값이 더 커지면 필요없으므로 진행 안하게 break
                break;
            }
        }
    }
    return count;       // 연속으로 더한 값들의 count 반환
}

//출처 : https://programmers.co.kr/learn/courses/30/lessons/12924
// 이게 가장 효율도 문제없이 한것 같습니다....


//피드백 받아서 수정
function solution(n) {
    let answer=0;
    let count=0;
    for(let i=1;i<=n;i++)
    {
        answer=0;
        for(let j=i;j<=n && n > answer; j++) {
            answer+=j;      // i부터 하나씩 계속 더하기
            if (answer === n)
                count += 1;
        }
    }
    return count;
}
