const http = require('http');
const fs = require('fs');
const path = require('path');

const port = process.env.PORT || 8100;
const logFile = path.join(__dirname, 'boot.log');

fs.writeFileSync(logFile, 'PERSISTENT TEST: Node.js starting at ' + new Date().toISOString() + '\n');
fs.appendFileSync(logFile, 'Port: ' + port + '\n');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Minimal server working\n');
});

server.listen(port, '0.0.0.0', () => {
    console.log('Server listening on port', port);
    fs.appendFileSync(logFile, 'Server listening on port ' + port + '\n');
});
