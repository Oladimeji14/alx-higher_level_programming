#!/usr/bin/node
const request = require('request');
const targetUrl = process.argv[2];

request(targetUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('Status code:', response.statusCode);
  }
});
