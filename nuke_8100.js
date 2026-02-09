const { exec } = require('child_process');

console.log("💣 Nuking Port 8100...");

console.log("💣 Nuking ALL Node processes...");

exec('ps aux | grep node | grep -v grep', (err, stdout, stderr) => {
    if (err || !stdout) {
        console.log("✅ No Node processes found. Starting bot...");
        startBot();
        return;
    }

    const lines = stdout.trim().split('\n');
    console.log(`⚠️ Found ${lines.length} Node processes. Killing them...`);

    lines.forEach(line => {
        const parts = line.trim().split(/\s+/);
        const pid = parts[1]; // PID is usually the second column
        if (pid) {
            try {
                process.kill(pid, 'SIGKILL');
                console.log(`💀 Killed PID ${pid}`);
            } catch (e) {
                console.log(`❌ Failed to kill ${pid}: ${e.message}`);
            }
        }
    });

    setTimeout(startBot, 2000);
});

function startBot() {
    console.log("🚀 Starting Bot on Port 8100...");
    const { spawn } = require('child_process');
    const bot = spawn('node', ['server.js'], {
        env: { ...process.env, PORT: 8100 },
        stdio: 'inherit'
    });
}
