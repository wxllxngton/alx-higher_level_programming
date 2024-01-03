#!/usr/bin/node
/**
 * Script that displays the status code of a GET request using the request module.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length != 3) {
  console.log(`Usage: ./${process.argv[1]} url`);
  exit(1);
}

/**
 * Function to handle the response of a GET request and print the status code.
 *
 * @param {Error} error - The error, if any, that occurred during the request.
 * @param {Object} response - The response object containing information about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function does not return a value.
 */
const printStatusCode = function (error, response, body) {
  console.log(`code: ${response.statusCode}`);
};

request(process.argv[2], printStatusCode);
