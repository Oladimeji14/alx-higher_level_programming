#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
let parsedData;
let filmCount = 0;

request(apiUrl, function (error, response, responseData) {
  if (error) {
    console.error(error);
  } else {
    parsedData = JSON.parse(responseData);
    parsedData.results.forEach(function (result) {
      result.characters.forEach(function (characterUrl) {
        const urlSegments = characterUrl.split('/');
        if (urlSegments[urlSegments.length - 2] === '18') {
          filmCount++;
        }
      });
    });
    console.log(filmCount);
  }
});
