#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const apiUrl = process.argv[2];
const outputFile = process.argv[3];

request(apiUrl, function (error, response, responseData) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(outputFile, responseData, 'utf8', function (writeError) {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
