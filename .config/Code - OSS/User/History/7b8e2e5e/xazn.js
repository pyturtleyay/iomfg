const { error } = require('console');

const fs = require('fs');




fs.writeFile('blog.txt', 'hellooo');
fs.readFile('blog.txt', 'utf8', function(err, data) {
  if (err){
    console.log(err);
  }
  console.log('OK: ' + 'blog.txt');
  console.log(data)
});


console.log("Hello world");

