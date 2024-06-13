#!/usr/bin/node
const request = require('request');
const filmID = parseInt(process.argv[2]);
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + filmID;
let responseBody;

request(apiUrl, function (error, response, responseData) {
  if (error) {
    console.error(error);
  } else {
    responseBody = JSON.parse(responseData);
    console.log(responseBody.title);
  }
});
