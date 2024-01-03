#!/usr/bin/node
/**
 * Script that gets the contents of a webpage
 * and stores it in a file.
 */

const request = require('request');
const fs = require('fs');
const { exit } = require('process');

if (process.argv.length !== 4) {
    console.log(`Usage: ./${process.argv[1]} url file_path`);
    exit(1);
}

/**
 * Scraps and returns a webpage's content.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * information about the request.
 * @param {string} body - The body of the response.
 * @returns {string} - The function return the contents of the webpage.
 */
const getPageContent = function (error, response, body) {
    if (error) {
        console.error(error);
        exit(1);
    }

    exportToPath(body);
};

/**
 * Stores the passed in contents in a file.
 *
 * @param {string} content - The content to be stored in the file
 * @returns {void} - The function returns nothing.
 */
const exportToPath = function (content) {
    fs.writeFile(
        process.argv[3],
        content,
        {
            encoding: 'utf-8',
            flag: 'w',
            mode: 0o666,
        },
        (error) => {
            if (error) {
                console.error(error);
            }
        }
    );
};

request(process.argv[2], getPageContent);
