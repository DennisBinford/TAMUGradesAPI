const express = require('express')
const router = express.Router()

const Section = require('../models/sectionschema')

router.get('/', (req, res) => {
    Section.find()
    .then(data => res.send(data))
    .catch(err => console.log(err))
})

router.get('/:department', (req, res) => {
    Section.find({Department : {'$regex' : req.params.department}})
    .then(data => {
        if(data)
            res.send(data)
        else
        res.status(404).json({error: 'no record with given department : ' + req.params.department})
    })
    .catch(err => console.log(err))
})

router.get('/:department/:course', (req, res) => {
    Section.find({Department : {'$regex' : req.params.department}, Course: {'$regex' : req.params.course}})
    .then(data => {
        if(data)
            res.send(data)
        else
        res.status(404).json({error: 'no record with given department and course : ' + req.params.department + ' ' + req.params.course})
    })
    .catch(err => console.log(err))
})

module.exports = router