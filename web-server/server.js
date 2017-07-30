const express = require('express')
const app = express()

function helloWorld(req, res) {
    res.send('Hello World!')
    console.log("Works")
}

app.post('/alarm', helloWorld)

app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
})