#!/usr/bin/node
// displaying ama character yose ya buri episode
const request = require('request');
const movieId = process.argv[2];
const inziraUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(inziraUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  movieData.characters.forEach(characterUrl => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error(`Error: ${charResponse.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
