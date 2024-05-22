#!/usr/bin/node
// printing the episode name of the passed arg int
const request = require('request');
const epId = process.argv[2];
const inzira = `https://swapi-api.alx-tools.com/api/films/${epId}`;
request(inzira, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
  } else {
    const dat = JSON.parse(body);
    console.log(dat.title);
  }
});
