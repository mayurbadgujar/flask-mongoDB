const express = require('express')
const app = express();
const axios = require('axios');
app.use(express.urlencoded({ extended: true }));
app.use(express.static('templates'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/templates/index.html');
  });

  
app.post('/submit', async (req, res) => {
try {
    const response = await axios.post('http://127.0.0.1:5000//submit', req.body);
    res.send(response.data);
} catch (error) {
    res.status(500).send('Error submitting form');
}
});


app.listen(3000, () => {
console.log('Frontend server running on http://localhost:3000');
});