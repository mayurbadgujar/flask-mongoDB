const express = require('express')
const app = express();
const axios = require('axios');
app.use(express.urlencoded({ extended: true }));
app.use(express.static('templates'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/templates/index.html');
});

app.get('/todo', (req, res) => {
    res.sendFile(__dirname + '/templates/todo.html');
});

app.post('/submit', async (req, res) => {
    try {
        const response = await axios.post('http://backend:5000/submit', req.body);
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error submitting form');
    }
});


app.post('/submittodoitem', async (req, res) => {
    try {
        const response = await axios.post('http://backend:5000/submittodoitem', req.body);
        debugger;
        res.send(response.data);
    } catch (error) {
        res.status(500).send('Error submitting form');
    }
});


app.listen(3000, () => {
    console.log('Frontend server running on http://localhost:3000');
});