#!/usr/bin/node
// js script to write contents to a file
const f = require('fs');
const fil = process.argv[2];
const dat = process.argv[3];
f.writeFile(fil, dat, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
