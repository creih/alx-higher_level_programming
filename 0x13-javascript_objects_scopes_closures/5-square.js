#!/usr/bin/node
const rect = require('./Rectangle');

class Square extends rect {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
