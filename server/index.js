const express = require("express");
const connect = require("./config/database");
const cors = require("cors");
const app = express();
const port = process.env.port || 4000;
const Attendance = require("./models/Attendance");
const guc = require("./models/Guc");
const nonguc = require("./models/Nonguc");

connect();

app.use(express.json({ extended: false }));
app.use(express.urlencoded({ extended: false }));
app.use(cors());

app.get("/checkAttendance/:userID", async (req, res) => {
  console.log(req.params);
  const { userID } = req.params;
  const gucExists = await guc.find({ userId: userID });
  const nongucExists = await nonguc.find({ userId: userID });
  if (gucExists.length !== 0 || nongucExists.length !== 0) {
    const Atten = await Attendance.find({ userID: userID });
    res.status(200).send((Atten ? Atten.length : 0) + " ");
  } else {
    res.status(400).send("User not found");
  }
});

app.put("/updateAttendance", async (req, res) => {
  const userID = req.body.userID;
  const gucExists = await guc.find({ userId: userID });
  const nongucExists = await nonguc.find({ userId: userID });
  if (gucExists.length !== 0 || nongucExists.length !== 0) {
    const newAtten = new Attendance({ userID: userID });
    newAtten.save();
    res.status(200).send("Attendance updated");
  } else res.status(400).send("User not found");
});

app.get("/getAttendances", async (req, res) => {
  res.send(await Attendance.find());
});

app.listen(port);
