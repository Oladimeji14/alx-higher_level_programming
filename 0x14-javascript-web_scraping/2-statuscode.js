t request = require('request');
const url = process.argv[2];

request(url, function (err, res, data) {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', res.statusCode);
  }
});
