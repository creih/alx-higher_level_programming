#!/usr/bin/node
/* function to add 2 args retrieved from terminal */
const iya1 = parseInt(process.argv[2]);
const iya2 = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(iya1, iya2));
