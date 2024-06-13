#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
let jsonResponse;
const taskCounts = {};

request(apiUrl, function (error, response, responseData) {
  if (error) {
    console.error(error);
  } else {
    jsonResponse = JSON.parse(responseData);
    jsonResponse.forEach(function (task) {
      if (task.completed === true) {
        const userId = task.userId;
        if (!(userId in taskCounts)) {
          taskCounts[userId] = 0;
        }
        taskCounts[userId] += 1;
      }
    });
    console.log(taskCounts);
  }
});
