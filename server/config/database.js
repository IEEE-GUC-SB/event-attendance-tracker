const mongoose = require("mongoose");
require("dotenv").config();

const mongoURL = process.env.mongoURL;

const connect = async () => {
  try {
    await mongoose.connect(mongoURL);
    console.log("database connected");
  } catch (err) {
    console.log(err);
  }
};

module.exports = connect;
