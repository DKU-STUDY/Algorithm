/* Counting the Number of Divisors O(√n) */

function divisors(n) {
  let i = 1;
  let result = 0;
  while (i * i < n) {
    if (n % i == 0)
      result += 2;
    i += 1;
  }
  if (i * i == n)
    result += 1;
  return result;
}
// console.log(divisors(36));

/* 10.2 Primality test — O(√n) */
function primality(n) {
  let i = 2;
  while (i * i <= n) {
    if (n % i == 0)
      return false;
    i += 1;
  }
  return true;
}
// console.log(primality(5));

/* 10.3: Reversing coins — O(n log n) */
function coins(n) {
  let result = 0;
  let coin = new Array(n + 1).fill(0);
  for (let i = 1; i < n + 1; i++) {
    let k = i;
    while (k <= n) {
      coin[k] = (coin[k] + 1) % 2;
      k += i
    }
    result += coin[i]
  }
  return result;
}
console.log(coins(10));
