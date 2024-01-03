#!/usr/bind/node
/**
 * Script that prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length != 3) {
    console.log(`Usage: ./${process.argv[1]} movieId`);
}

/**
 * Prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * informations about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function does not return a value.
 */
const printTitle = function (error, response, body) {
    const data = response.json();
    console.log(data.title);
};

request(
    `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
    printTitle
);
