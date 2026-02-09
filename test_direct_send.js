const fetch = require('node-fetch');

async function testSend() {
    const url = 'https://dalaalstreetss.alwaysdata.net/send-otp?phone=918287761013&message=Manual+Test+from+Antigravity';
    console.log('Testing direct send to:', url);

    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log('Response:', data);
    } catch (error) {
        console.error('Error:', error.message);
    }
}

testSend();
