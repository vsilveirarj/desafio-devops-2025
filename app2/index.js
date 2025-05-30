require('./tracing');

const express = require('express');
const redis = require('redis');
const app = express();
const port = 3000;

const client = redis.createClient({
    url: 'redis://redis:6379'
});
client.connect();

app.get('/ping', (req, res) => {
    res.json({ message: 'App 2 - OK' });
});

app.get('/time', async (req, res) => {
    const cacheKey = 'app2_time';
    const cached = await client.get(cacheKey);
    if (cached) {
        return res.json({ time: cached });
    }
    const currentTime = new Date().toISOString();
    await client.setEx(cacheKey, 60, currentTime);
    res.json({ time: currentTime });
});

app.listen(port, () => {
    console.log(`App 2 listening at http://localhost:${port}`);
});
