const http = require('http');

const ports = [3000, 8000, 8100, 8300];

async function checkPort(port) {
    return new Promise((resolve) => {
        const server = http.createServer();

        server.once('error', (err) => {
            console.log(`❌ Port ${port} is BUSY or BLOCKED (${err.code})`);
            resolve(false);
        });

        server.once('listening', () => {
            console.log(`✅ Port ${port} is OPEN and USABLE`);
            server.close(() => resolve(true));
        });

        server.listen(port, '0.0.0.0');
    });
}

async function run() {
    console.log("🔍 Scanning for usable ports...");
    for (const p of ports) {
        await checkPort(p);
    }
}

run();
