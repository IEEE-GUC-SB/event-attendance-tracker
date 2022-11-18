const mongoose = require("mongoose");

const attendanceSchema = new mongoose.Schema(
  {
    userID: {
      type: String,
    },
  },
  { timestamps: true }
);
const Attendance = mongoose.model("Attendance", attendanceSchema);
module.exports = Attendance;
