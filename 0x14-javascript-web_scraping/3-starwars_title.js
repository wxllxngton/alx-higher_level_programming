#!/usr/bin/node
/**
 * Script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length !== 3) {
  console.log(`Usage: ./${process.argv[1]} movieId`);
  exit(1);
}

/**
 * Prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * information about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function does not return a value.
 */
const printTitle = function (error, response, body) {
  const data = JSON.parse(body);
  console.log(data.title);
};

request(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    printTitle
);
