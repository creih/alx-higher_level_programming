#!/usr/bin/node
/* task 7 about looping C is fun x tymz */
const iya1 = process.argv[2];
const x = parseInt(iya1);
if (!isNaN(x)) {
  let i = 0;
  for (i; i < x; i++) {
    console.log('C is fun');
  }
}
else {
  console.log('Missing number of occurences')
}
