const mongoose = require('mongoose')

const sectionSchema = new mongoose.Schema({
    Department: {
        type: String,
        required: true
    },
    Course: {
        type: String,
        required: true
    },
    Semester: {
        type: String,
        required: true
    },
    Year: {
        type: String,
        required: true
    },
    Section: {
        type: String,
        required: true
    },
    Professor: {
        type: String,
        required: true
    },
    Grades: {
        type: Array,
        required: true
    },
})

module.exports = mongoose.model('Section', sectionSchema, 'AllSectionsTest')