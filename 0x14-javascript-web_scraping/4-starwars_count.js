#!/usr/bin/node
/**
 * Script that prints the number of movies where
 * the character “Wedge Antilles” is present.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length !== 3) {
  console.log(`Usage: ./${process.argv[1]} url`);
  exit(1);
}

/**
 * Prints the number of movies where the
 * character “Wedge Antilles” is present.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * information about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function does not return a value.
 */
const printOccurences = function (error, response, body) {
  if (error) {
    console.error(`Error: ${error.message}`);
    exit(1);
  }

  const parsedBody = JSON.parse(body);
  const films = parsedBody.results;

  let occurrences = 0;

  for (const film of films) {
    if (
      film.characters.includes(
        'https://swapi-api.alx-tools.com/api/people/18/'
      )
    ) {
      occurrences++;
    }
  }

  console.log(occurrences);
};

request(process.argv[2], printOccurences);
