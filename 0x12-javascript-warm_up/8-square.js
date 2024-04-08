#!/usr/bin/node
/* about printing a square of character usiin loops */
const iya1 = process.argv[2];
const ingano = parseInt(iya1);
if (!isNaN(ingano)) {
  for (let i = 0; i < ingano; i++) {
    let row = '';
    for (let j = 0; j < ingano; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
