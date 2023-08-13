const express = require('express')
const router = express.Router()

const Section = require('../models/sectionschema')

router.get('/', (req, res) => {
    Section.find()
    .then(data => res.send(data))
    .catch(err => console.log(err))
})

router.get('/:professor', (req, res) => {
    Section.find({Professor : {'$regex' : req.params.professor}})
    .then(data => {
        if(data)
            res.send(data)
        else
        res.status(404).json({error: 'no record with given professor : ' + req.params.professor})
    })
    .catch(err => console.log(err))
})

module.exports = router