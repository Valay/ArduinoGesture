
window.addEventListener('load', onloadHandler, false);

var canvas;
var ctx;

function canvasInit()
{
	
	canvas = document.getElementById('draw');
	ctx = canvas.getContext('2d');
    ctx.fillStyle = "rgb(200,0,0)";
	
	
}

function socketInit()
{	
	/*var socket = io.connect('http://localhost:4000');
	socket.on('data', function(data){
		console.log(data);
		drawData(data);
	});	*/
}

function drawData(data)
{
	x = canvas.width/2 + data.x;
	y = canvas.height/2 + data.y;
	r = 1;
	ctx.moveTo(x,y);
	ctx.arc(x, y, r, 0, 2*Math.PI, false);
	ctx.fillStyle = 'black';
    ctx.fill();
}

function onloadHandler()
{
	canvasInit();
	
	//socketInit();
	data = {};
	data.x = 0;
	data.y = 0;
	drawData(data);
	//setInterval( generateData,50);
}

function generateData()
{
	data.x = Math.random() * 500; 
	data.y = Math.random() * 500;
	drawData(data);	
}

function logAndParseData(logdata)
{
	//logdata = logdata.splice(',');
	
	for(i = 0; i < logdata.length; i++){
		splitdata = logdata[i].split(',');
		data.x = parseInt(splitdata[0]);
		data.y = parseInt(splitdata[1]);
		drawData(data);
	}
	
	console.log(logdata);

}
