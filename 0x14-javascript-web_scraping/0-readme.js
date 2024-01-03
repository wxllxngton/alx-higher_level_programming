#!/usr/bin/node
/*
Script that reads and prints the content of a file.
*/

const fs = require('fs');
const { exit } = require('process');

if (process.argv.length !== 3) {
  console.log(`Usage: ./${process.argv[1]} file_path`);
  exit(1);
}

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // If error occurred while reading the file
    exit(1);
  }

  console.log(data);
});
