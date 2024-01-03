#!/usr/bin/node
/**
 * Script that computes the number of tasks completed by user id.
 */

const request = require('request');
const { exit } = require('process');

if (process.argv.length !== 3) {
    console.log(`Usage: ./${process.argv[1]} url`);
    exit(1);
}

/**
 * Computes the number of tasks completed by user id
 * and prints users with completed tasks.
 *
 * @param {Error} error - The error, if any,
 * that occurred during the request.
 * @param {Object} response - The response object containing
 * information about the request.
 * @param {string} body - The body of the response.
 * @returns {void} - The function returns nothing.
 */
const computeCompletedTasks = function (error, response, body) {
    let tasks = {};

    if (error) {
        console.error(error);
        exit(1);
    }

    const todos = JSON.parse(body);

    for (const todo of todos) {
        if (todo['completed']) {
            if (todo['userId'] in tasks) {
                tasks[todo['userId']]++;
            } else {
                tasks[todo['userId']] = 1;
            }
        }
    }

    console.log(tasks);
};

request(process.argv[2], computeCompletedTasks);
