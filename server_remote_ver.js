const express = require('express');
const cors = require('cors');
const QRCode = require('qrcode');
const WhatsAppBot = require('./whatsapp');
const http = require('http');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 8300;
const logFile = path.join(__dirname, 'boot.log');

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const bot = new WhatsAppBot();

console.log('🚀 Starting DalaalStreet WhatsApp Bot...');
bot.initialize().catch(err => {
    const msg = `❌ Initialization failed: ${err.message}`;
    console.error(msg);
    try { fs.appendFileSync(logFile, `${msg}\n`); } catch (e) { }
});

app.get('/', (req, res) => {
    res.json({
        status: 'online',
        service: 'DalaalStreet WhatsApp OTP Bot',
        version: '2.5.0'
    });
});

app.get('/status', async (req, res) => {
    const status = bot.getStatus();

    if (!status.connected && status.qrCode) {
        try {
            const qrImage = await QRCode.toDataURL(status.qrCode);
            return res.send(`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>WhatsApp QR Code</title>
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <style>
                        body { font-family: sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; background: #f0f2f5; }
                        .card { background: white; padding: 2rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
                        img { margin-top: 1rem; max-width: 100%; border: 1px solid #ddd; }
                        h1 { color: #128c7e; }
                    </style>
                </head>
                <body>
                    <div class="card">
                        <h1>Link WhatsApp</h1>
                        <p>Scan this QR code with WhatsApp to connect:</p>
                        <img src="${qrImage}" alt="QR Code" />
                        <p style="margin-top: 1rem; font-size: 0.9rem; color: #666;">Settings > Linked Devices > Link a Device</p>
                    </div>
                    <script>setTimeout(() => location.reload(), 5000);</script>
                </body>
                </html>
            `);
        } catch (err) {
            console.error('Error generating QR image:', err);
        }
    }

    res.json(status);
});

app.all('/send-otp', async (req, res) => {
    try {
        const phone = req.query.phone || req.body.phone;
        const message = req.query.message || req.body.message;

        if (!phone || !message) {
            return res.status(400).json({ error: 'Missing phone or message' });
        }

        if (!bot.isConnected) {
            return res.status(503).json({ error: 'WhatsApp not connected. Visit /status' });
        }

        const result = await bot.sendMessage(phone, message);
        res.json(result);

    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

const server = http.createServer(app);
server.listen(PORT, '0.0.0.0', () => {
    const msg = `✅ Server listening on 0.0.0.0:${PORT}`;
    console.log(msg);
    try { fs.appendFileSync(logFile, `${msg}\n`); } catch (e) { }
});

process.on('uncaughtException', (err) => {
    try { fs.appendFileSync(logFile, `💥 Uncaught Exception: ${err.message}\n${err.stack}\n`); } catch (e) { }
    process.exit(1);
});
