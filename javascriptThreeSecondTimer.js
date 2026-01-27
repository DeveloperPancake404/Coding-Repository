setTimeout(() => {
	alert("This alert was after 3 seconds")
	console.log("This was after 3 seconds of the page being up")
	document.body.innerHTML += "<h1>Created after three seconds</h1>"
}, 3000);
