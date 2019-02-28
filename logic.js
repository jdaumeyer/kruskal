var canvas = document.getElementById("network");
var ctx = canvas.getContext("2d");

var canvasPosition = {
	x: 0,
	y: 0
}

canvas.on('click', function(e) {
	var mouse = {
		x: e.pageX - canvasPosition.x,
		y: e.pageY - canvasPosition.y
	}
	console.log("Click at x: " + mouse.x + ", y: " + mouse.y);
});

let node = new Node(50, 50)
node.draw();

