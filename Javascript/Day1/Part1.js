
function syncReadFile(filename) {
  const contents = readFileSync(filename, 'utf-8');
  const arr = contents.split(/\r?\n/);
  //console.log(arr);
  return arr;
}

function evaluateincrease(array){
if (placeholder < array){ placeholder = array; counter++;}
else { placeholder = array; }
}


// Start
const {readFileSync, promises: fsPromises} = require('fs');
const array = syncReadFile('.\\Javascript\\Day1\\input.txt');
let placeholder = 0, counter = 0;
array.forEach(evaluateincrease);
console.log(counter);



