const fs = require("fs");
const stringToWrite = "HELLO I AM WRITTEN TO THE FILE";

fs.writeFile("./test.txt", stringToWrite, (err) => {
if (err) {
    console.error(err);
return;
  }
});
console.log("Data has been Written");