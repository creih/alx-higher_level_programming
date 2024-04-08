#!/usr/bin/node
const iya1 = parseInt(process.argv[2]);
function factorial(n) {
  if(isNaN(n) || n === 0) {
    return (1);
  }
	return (n * factorial(n - 1));
}
const res = factorial(iya1);
console.log(res);
