#!/usr/bin/node
/**
 * Script that writes a string to a file.
 */

const fs = require('fs');
const { exit } = require('process');

if (process.argv.length !== 4) {
    console.log(`Usage: ./${process.argv[1]} file_path string_to_write`);
    exit(1);
}

fs.writeFile(
    process.argv[2],
    process.argv[3],
    {
        encoding: 'utf8',
        flag: 'w',
        mode: 0o666,
    },
    (error) => {
        if (error) {
            console.error(error);
            exit(1);
        }
    }
);
