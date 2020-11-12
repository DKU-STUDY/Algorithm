function solution (regs) {
  const account = [];

  const action = ([action, id, value]) => {
    const target = account.find(v => v.id === id);
    switch (action) {
      case 'DEPOSIT':
        return DEPOSIT(id, value, target);
      case 'CREATE':
        return CREATE(id, value, target);
      case 'WITHDRAW':
        return WITHDRAW(id, value, target);
    }
  };
  const CREATE = (id, max, target) => {
    if (target) return 403;
    account.push({ id, value: 0, max: ~~max });
    return 200;
  };
  const DEPOSIT = (id, value, target) => {
    if (target) {
      target.value += ~~value;
      return 200;
    }
    return 404;
  };
  const WITHDRAW = (id, value, target) => {
    if (target) {
      if (value > target.max) return 403;
      target.value -= ~~value;
      target.max -= ~~value;
      return 200;
    }
    return 404;
  };
  return regs.map(v => action(v.split(' ')));
}

console.log(
  solution(['DEPOSIT 3a 10000', 'CREATE 3a 300000', 'WITHDRAW 3a 150000', 'WITHDRAW 3a 150001']),
  // .toString() ===	[404, 200, 200, 403].toString(),
  solution(['CREATE 3a 10000', 'CREATE 3a 20000', 'CREATE 2bw 30000']).toString() === [200, 403, 200].toString(),
);