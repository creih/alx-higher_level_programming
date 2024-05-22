#!/usr/bin/node
// getting page content and writing tem to a file
const request = require('request');
const f = require('fs');
const inzira = process.argv[2];
const fil = process.argv[3];
request(inzira, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    f.writeFile(fil, body, 'utf-8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  }
});
