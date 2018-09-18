### node.js – getting data from serial port to web pages

Reference [article](https://itp.nyu.edu/physcomp/labs/labs-serial-communication/lab-serial-communication-with-node-js/). This article explains installation of node js.

1. In order to capture data from the serial port from arduino, raspberry pi etc., the following code gives the name of the usb port to which the external microcontroller is connected.
``` 
//    CODE TO GET SERIAL PORT
var serialport = require("serialport");
var SerialPort = serialport.SerialPort;
serialport.list(function (err, ports) {
ports.forEach(function(port) {
console.log(port.comName);
});
});
```

2. The following code is used to read from the serial port at a baud rate of 115200.   
	- Run the code using ‘node index.js’. The data is displayed in the terminal.  
	- Also, if the webpage with url as localhost:3000/data is refreshed, this data is displayed in the webpage.  
```
var serialport = require('serialport'),// include the library
SerialPort = serialport.SerialPort,    // make a local instance of it
portName ="/dev/ttyACM0"; //process.argv[2];            // get port name from the command line

var serialData = 0;                    // latest data saved from the serial port
var serialShow = "";
var serialFile = "";
var tempData = "";

var fs = require('fs');
var j =0;
var servi = require('servi');          // include the servi library

var app = new servi(false);            // servi instance
app.port(3000);                        // port number to run the server on

// configure the server's behavior:
app.serveFiles("public");              // serve all static HTML files from /public
app.route('/data', sendData);          // route requests for /data to sendData() function
// now that everything is configured, start the server:
app.start();

var myPort = new SerialPort(portName, {
baudRate: 115200,
// look for return and newline at the end of each data packet:
parser: serialport.parsers.readline('\r\n')
});

// these are the definitions for the serial events:
myPort.on('open', showPortOpen);
myPort.on('data', saveLatestData);
myPort.on('close', showPortClose);
myPort.on('error', showError);

// these are the functions called when the serial events occur:
function showPortOpen() {
console.log('port open. Data rate: ' + myPort.options.baudRate);
}

function saveLatestData(data) {
// console.log(data);
if(data.search("Time") == 0){
serialShow = data;
serialFile = serialData;
serialData = "";
if(j==5){j=0;
fs.writeFile("/opt/lampp/htdocs/medical/ecg.csv", serialFile);}
j++;
}
if(data.search("Temp") == -1){
serialData = serialData + data + "\n";
}else{
tempData = data;
}
}

function showPortClose() {
console.log('port closed.');
}

function showError(error) {
console.log('Serial port error: ' + error);
}

// ------------------------ Server function
function sendData(request) {
// print out the fact that a client HTTP request came in to the server:
console.log("Got a client request, sending them the data.");
// respond to the client request with the latest serial string:
request.respond(tempData);
}
```
