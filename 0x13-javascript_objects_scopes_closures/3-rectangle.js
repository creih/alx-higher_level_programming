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
      for (let j = 0; j < this.width; j++) {
        console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
