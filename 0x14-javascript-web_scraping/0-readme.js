#!/usr/bin/node
# js script to read file contents
const f = require('fs');
const fil = process.argv[2];
f.readFile(fil, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
