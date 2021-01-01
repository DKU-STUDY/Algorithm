function solution(array, commands) {
    let answer = [];
    
    for(let i =0; i < commands.length; i++){
        let sliced_arr = (array.slice(commands[i][0]-1, commands[i][1]));
        //아래에서 그냥 sliced_arr.sort()를 하게 되면 2번이 안 풀린다. 
        sliced_arr.sort((a, b) => a - b)
        let num = sliced_arr[commands[i][2]-1];
        answer.push(num);
    }
    return answer;
}


// >문제풀이방법
// slice함수를 통해 배열의 일부분을 선택하여 새로운 배열로 만들었다.
// 그 후 sort함수로 정렬을 해주고 
// 그 안에서 k번째 숫자를 찾아 배열에 push해주면 된다. 

// >헷갈린점
// 1. 문제에서 2번쨰 ~ 5번째라고 했지만, 실제 배열에선 [1] , [4] 였다. 
//  -> console.log()를 통해 편하게 알 수 있었다! 

// 2. sort함수 , 뒤에 sortFunction도 넣어줘야한다
//  -> 아무것도 안 넣으면 배열 각 요소를 문자열로 변환하고 유니코드값에 따라 정렬한다. 
//  -> 즉, 여기선 숫자를 또 문자열로 변환해서 유니코드값에 따라 정렬하기 때문에 어떤 경우는 문제가 될 수 있었다
//  -> 따라서 숫자 배열을 정렬할 때는 반드시 함수 "(a, b) => a - b" 를 넣어준다(오름차순)
//  출처: https://fluorite94.tistory.com/220
// 3. array(배열)은 push 함수를 통해 넣는다! "+=" 이건 string의 경우에 사용! 

// junihwang.js 참고 

// return commands.map(([i, j, k]) => array.slice(i-1, j).sort((a, b) => a- b)[k-1])

// 코드 보고 감탄했네요..!
// map은 배열에 접근해 각 요소들에게 행한 값들을 따로 배열로 만드는 것이다. 
// 이 경우 2차원 배열에 접근해 각 [0],[1],[2]를 i,j,k로 명칭하고
// 각각 i,j,k를 용도에 맞게 사용해서 나오는 값들을 따로 배열로 만들어주는, 이 문제에 아주 적합한 용도이다. 
