#!/usr/bin/node
// counting inshuro wedge antiles iri present
const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = 18;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log(`Error: ${response.statusCode}`);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    data.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
