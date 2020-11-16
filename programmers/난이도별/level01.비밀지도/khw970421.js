//처음 성공한 코드 (for문에 난잡)
function solution(n, arr1, arr2) {
    let answer = [];
    let number,length=arr1.length;
    let Sarr1 =[];
    let Sarr2 = [];
    for(let i=0;i<length;i++)
        Sarr1.push(arr1[i].toString(2).padStart(length,'0'));
    for(let i=0;i<length;i++)
        Sarr2.push(arr2[i].toString(2).padStart(length,'0'))
    console.log(Sarr1,Sarr2)

    for(let i=0;i<length;i++)
    {
        answer[i]=''
    }


    for(let i=0;i<length;i++)
    {
        for(let j=0;j<length;j++)
        {
            if(Sarr1[i][j]==0&&Sarr2[i][j]==0)
                answer[i]+=' '
            else
                answer[i]+='#'
        }
    }
    console.log(answer)
    return answer;
}


// 수정한코드
function solution(n, arr1, arr2) {
    let answer = [],Sarr1 =[],Sarr2 = [];
    const length=arr1.length;

    for(let i=0;i<length;i++){                                      //2진수로 만든 각각을 부족한 길이만큼 0을 앞에 채우기
        Sarr1.push(arr1[i].toString(2).padStart(length,'0'));
        Sarr2.push(arr2[i].toString(2).padStart(length,'0'));
    }

    for(let i=0;i<length;i++)                                       //갯수만큼 만들어놓기
        answer[i]=''

    for(let i=0;i<length;i++)
        for(let j=0;j<length;j++)
            (Sarr1[i][j]==0&&Sarr2[i][j]==0) ? answer[i]+=' ' : answer[i]+='#'      //둘다 0이면 공백 아니면 #으로 값지정

    return answer;
}

// 다른 코드 분석 : 비슷하게 padStart를 사용하였지만 map으로 for문을 대체하고  정규화식으로 나머지 숫자를 변환하는게 인상깊었음
function solution(n, arr1, arr2) {
    return arr1.map((a,i)=>(a|arr2[i]).toString(2).padStart(n,0).replace(/0/g,' ').replace(/1/g,'#'))
}
