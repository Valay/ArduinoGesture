/**
 * Module dependencies.
 */
var express = require('express');
var connect = require('connect');
var http = require('http');
var path = require('path');
var jade = require('jade');
var stylus = require('stylus');
var markdown = require('markdown').markdown;
var app = express();
var fs = require('fs');

// all environments
app.set('port', process.env.PORT || 4000);
app.set('views', path.join(__dirname, 'views'));

//app.engine('html', require('jade').renderFile);

app.set('view engine', 'jade');
app.use(express.cookieParser());
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')))
app.use('/public', express.static(__dirname + '/public'));
app.get('/*', function(req, res, next){ 
  res.setHeader('Last-Modified', (new Date()).toUTCString());
  next(); 
});
//app.set('')

app.use(function(req, res, next){
  res.render('404', { status: 404, url: req.url });
});

app.configure('development', function() {
  app.set('db-uri', 'mongodb://localhost/deftdraftjs');
  app.use(express.errorHandler({ dumpExceptions: true }));
  app.set('view options', {
    pretty: true
  });
});

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

app.get('/', function(req, res){	
	res.render('draw.jade');
});

var server = app.listen(4000);
var io = require('socket.io').listen(server);

io.sockets.on('connection', function (socket) {
  socket.emit('connected', { hello: 'world' });
  
  socket.on('nextdata', function(data){
  	setTimeout(function(){
	  	nextdata = waitForNextData();
	  	console.log(nextdata); 	
	  	socket.emit('data', {data: nextdata });
	  }, 100);
  })
});

function waitForNextData()
{
	var nextdata;
	
	/*fs.readFile('test.json', function(err, data){
		if(err)
			throw err;
		text = data.toString();
		text = text.split('\n');
		nextdata = text;
		console.log(nextdata);
		/*console.log(text);
		/*fs.writeFile('test.json', '', function(err, write){
			if(err)
				throw err;
			console.log("File written");
		});
	});
	*/
	data = fs.readFileSync('test.json');
	nextdata = data.toString();
	nextdata = nextdata.split('\n');

	// fs.writeFileSync('test.json','');
			
	console.log(nextdata);
	return nextdata;
}