var submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", function() {
	var fileInput = document.getElementById("file-input");
	var textarea = document.getElementById("textarea");
	var file = fileInput.files[0];
	var description = textarea.value;
	


	if (file || description) {
		
		 location.href="http://127.0.0.1:5501/templates/result.html";
		 const fs = require("fs");
// const stringToWrite = "HELLO I AM WRITTEN TO THE FILE";

fs.writeFile("test.txt", description, (err) => {
if (err) {
    console.error(err);
return;
  }
});
// console.log("Data has been Written");
	 

	} else  {
		alert("Please choose a file or enter a description.");
	}
	
});



