function setup() {
	let image_size_px = 2000
	createCanvas(image_size_px, image_size_px);

	}

function draw() {
	let image_size_px = 2000

	let points = [];
	starting_pos = [[0, image_size_px* 0.50], [image_size_px, image_size_px*0.50]]
	x = 0
	y = image_size_px *0.50
	for (let _ = 0; _ < 10; _++){
		x += 200
		y += (100 - Math.floor(Math.random(image_size_px*0.4)))
		if (y >= image_size_px*0.4){
			y -= 300 
		}elseif (y <= image_size_px*0.4){
			y += 300
		}
		let newpoints = [x, y]
		points.push(newpoints)
		x -= 200
		y -= (100 - Math.floor(Math.random(image_size_px*0.4)))
		let newpoints = [x, y]
		points.push(newpoints)
		ellipse
		
	}
}