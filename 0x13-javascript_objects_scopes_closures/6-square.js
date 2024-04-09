#!/usr/bin/node
const ojsq = require('./5-square');
class Square extends ojsq {
  charPrint (c) {
    if (isNaN(c)) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
