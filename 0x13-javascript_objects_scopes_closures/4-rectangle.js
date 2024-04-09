#!/usr/bin/node
/* task 3 */
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (!this.width || !this.height) {
      console.log('');
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  rotate () {
    let tp = this.width;
    this.width = this.height;
    this.height = tp;
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
