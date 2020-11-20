function solution(numbers) {
  var answer = [];
  
  for(var i=0; i < numbers.length; i++)
      {
          for(var j= 1; j <numbers.length; j ++)
              {
                  if(j != i)
                      answer.push(numbers[i] + numbers[j]);  
              }
         
      }
  const ans = new Set(answer);
  answer = [ ...ans ];
  answer.sort((a,b) => { return(a-b);})
  return answer;
}