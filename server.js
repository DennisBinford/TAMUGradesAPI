require('dotenv').config()
const express = require('express')
const mongoose = require('mongoose')

const port = process.env.port || 3000
const connectDB = require('./db.js')
const sectionRouter = require('./routes/sectionroute')
const professorRouter = require('./routes/professorroute')

const app = express()
app.use('/', sectionRouter)
app.use('/professor', professorRouter)

connectDB()
    .then(() => {
        console.log('Successful database connection')
        app.listen(port)
    })
    .catch(err => console.log(err))



