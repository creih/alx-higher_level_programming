#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }
  function print () {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        console.log('x');
      }
    }
  }
}
module.exports = Rectangle;
