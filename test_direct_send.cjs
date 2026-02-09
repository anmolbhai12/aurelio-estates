const https = require('https');

const url = 'https://dalaalstreetss.alwaysdata.net/send-otp?phone=918287761013&message=Direct+Bot+Test+from+DalaalStreet';

console.log('Sending request to:', url);

https.get(url, (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        console.log('Response Status:', res.statusCode);
        console.log('Body:', data);
    });
}).on('error', (err) => {
    console.error('Error:', err.message);
});
