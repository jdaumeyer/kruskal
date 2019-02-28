class Node {
	x;
	y;
	connectedNodes = [];
	constructor(x, y) {
		this.x = x;
		this.y = y;
	}

	addConnection(node) {
		
	}

	draw(ctx) {
		ctx.fillStyle="#0000FF";
		ctx.beginPath();
		ctx.arc(100, 75, 50, 0, 2 * Math.PI);
		ctx.stroke();
		ctx.endPath();
	}
	
}



