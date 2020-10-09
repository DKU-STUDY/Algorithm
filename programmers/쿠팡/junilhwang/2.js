function solution (n, customers) {
  const kiosks = Array(n).fill(0);
  const matches = Array(n).fill(0);

  let beforeDate = null;
  let year = 2020;
  for (const customer of customers ) {
    const [date, start, minute] = customer.split(' ');
    if (beforeDate && beforeDate !== date && date === '01/01') {
      year += 1;
    }
    const timestamp = new Date(`${year}/${date} ${start}`).getTime();
    const end = timestamp + (1000 * 60 * minute);
    const selectedIndex = kiosks.reduce(([min, minK], v, k) => {
      return v < min ? [v, k] : [min, minK];
    }, [Infinity, -1])[1];

    kiosks[selectedIndex] = end;
    matches[selectedIndex] += 1;

    beforeDate = date;
  }

  return Math.max(...matches);
}

console.log(
  solution(3,
    ['10/01 23:20:25 30',
      '10/01 23:25:50 26',
      '10/01 23:31:00 05',
      '10/01 23:33:17 24',
      '10/01 23:50:25 13',
      '10/01 23:55:45 20',
      '10/01 23:59:39 03',
      '10/02 00:10:00 10']), 4);
console.log(
  solution(2,
    ['02/28 23:59:00 03',
      '03/01 00:00:00 02',
      '03/01 00:05:00 01']), 2);