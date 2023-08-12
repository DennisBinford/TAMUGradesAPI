require('dotenv').config()
const express = require('express')
const mongoose = require('mongoose')

const connectDB = require('./db.js')
const sectionRouter = require('./routes/sectionroute')
const professorRouter = require('./routes/professorroute')

const app = express()
app.use('/api/section', sectionRouter)
app.use('/api/professor', professorRouter)

connectDB()
    .then(() => {
        console.log('Successful database connection')
        app.listen(3000)
    })
    .catch(err => console.log(err))



