const mongoose = require('mongoose')
const dbURI = process.env.DATABASE_URI

module.exports = () => {
    return mongoose.connect(dbURI)
}
