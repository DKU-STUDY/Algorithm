function solution(numbers) {
    const plus_num=[];
    const number_length= numbers.length;
    for(let i=0;i<number_length;i++)
        for(let j=i+1;j<number_length;j++)
            plus_num.push(numbers[i]+numbers[j]);       //2개씩 더한것을 넣기
    plus_num.sort((A,B)=>(A-B));        //정렬하기
    return [...new Set(plus_num)];      //중복된 값 처리하고 return
}



console.log(JSON.stringify(solution([2, 1, 3, 4, 1]))==JSON.stringify([2, 3, 4, 5, 6, 7]));
console.log(JSON.stringify(solution([5, 0, 2, 7]))==JSON.stringify([2, 5, 7, 9, 12]));
