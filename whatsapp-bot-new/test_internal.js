const http = require('http');

console.log('Testing internal reachability of http://localhost:8300/status...');

http.get('http://localhost:8300/status', (res) => {
    let data = '';
    res.on('data', (chunk) => { data += chunk; });
    res.on('end', () => {
        console.log('✅ Internal Request Successful!');
        console.log('Status Code:', res.statusCode);
        console.log('Response:', data);
    });
}).on('error', (err) => {
    console.error('❌ Internal Request Failed:', err.message);

    console.log('Retrying with 127.0.0.1...');
    http.get('http://127.0.0.1:8300/status', (res) => {
        let data = '';
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
            console.log('✅ Internal Request (127.0.0.1) Successful!');
            console.log('Status Code:', res.statusCode);
            console.log('Response:', data);
        });
    }).on('error', (err2) => {
        console.error('❌ Both localhost and 127.0.0.1 failed:', err2.message);
    });
});
