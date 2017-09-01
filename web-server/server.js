const express     = require('express')
const bodyParser  = require('body-parser')
const MongoClient = require('mongodb').MongoClient

const app = express()

let db

MongoClient.connect('mongodb://localhost:27017/test', (err, database) => {
    if (err) console.log(err)
    db = database
    app.listen(8008, () => {
        console.log('Example app listening on port 8008!')
    })
})


app.use(bodyParser.json())

app.get('/', (req, res) => {
    let cursor = db.collection('alarm').find().toArray((err, results) => {
        console.log(results)
    })
})

app.post('/alarm', (req, res) => {
    console.log(req.body)
    db.collection('alarm').save(req.body, (err, result) => {
        if (err) return console.log(err)
        console.log('saved to database')
    })
})