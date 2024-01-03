#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length !== 3) {
  console.log(`Usage: ./${process.argv[1]} movieId`);
  exit(1);
}

const characters = [];

/**
 * Prints all characters of a Star Wars movie.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * information about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function returns nothing.
 */
const printAllCharacters = function (error, response, body) {
  if (error) {
    console.error(error);
    exit(1);
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;

  // Function to handle each character request
  const handleCharacterRequest = function (characterUrl) {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        exit(1);
      }

      const data = JSON.parse(body);
      const characterName = data.name;
      characters.push(characterName);

      // Print character name after adding to the list
      console.log(characterName);
    });
  };

  // Make requests for each character URL
  characterUrls.forEach(handleCharacterRequest);
};

request(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`,
    printAllCharacters
);
