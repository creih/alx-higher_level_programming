#!/usr/bin/node
// displaying the staus of get request
const request = require('request');
const inzira = process.argv[2];
request(inzira, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log('code:', response.statusCode);
  }
});
