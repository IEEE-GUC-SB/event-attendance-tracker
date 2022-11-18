const mongoose = require("mongoose");

const gucSchema = new mongoose.Schema({}, { strict: false });
const guc = mongoose.model("guc", gucSchema);
module.exports = guc;
