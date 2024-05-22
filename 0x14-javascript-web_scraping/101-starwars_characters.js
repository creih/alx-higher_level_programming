#!/usr/bin/node
// same as task 100 ariko iyi yo ordering stays the same
const req = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

req(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;

  const printCharacters = () => {
    if (charactersUrls.length === 0) {
      console.log("No characters found for this movie.");
      return;
    }

    let charactersPrinted = 0;

    charactersUrls.forEach(characterUrl => {
      req(characterUrl, (charError, charResponse, charBody) => {
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

        charactersPrinted++;
        if (charactersPrinted === charactersUrls.length) {
          process.exit();
        }
      });
});
  };

  printCharacters();
});
