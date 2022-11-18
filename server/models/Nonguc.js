const mongoose = require("mongoose");

const nongucSchema = new mongoose.Schema({}, { strict: false });
const nonguc = mongoose.model("nonguc", nongucSchema);
module.exports = nonguc;
