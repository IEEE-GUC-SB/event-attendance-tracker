import "./App.css";
import { useState, useRef } from "react";
import { Button } from "react-bootstrap";
import Card from "react-bootstrap/Card";
import Form from "react-bootstrap/Form";
import "bootstrap/dist/css/bootstrap.min.css";
import axios from "axios";
import proxy from "./proxy.json";
import "./App.css";
function App() {
  const inputRef = useRef();
  const [attendance, setAttendance] = useState();
  const [message, setMessage] = useState();
  function handleCheck() {
    setMessage("");
    setAttendance("");
    axios
      .get(proxy.URL + "/checkAttendance/" + inputRef.current.value)
      .then(function (response) {
        setAttendance("Your attendance: " + parseInt(response.data));
        setMessage("");
      })
      .catch((err) => {
        setAttendance("User not found");
        setMessage("");
      });
  }
  function handleTake() {
    setMessage("");
    setAttendance("");
    axios
      .put(proxy.URL + "/updateAttendance", { userID: inputRef.current.value })
      .then(function (response) {
        setAttendance("");
        setMessage("Attendance updated");
      })
      .catch((err) => {
        setAttendance("");
        setMessage("User not found");
      });
  }

  return (
    <div className="wrapper">
      <div className="header">
        <img className="image" src="1562011013730.png"></img>
      </div>
      <div className="big-container">
        <Card>
          <Card.Body>
            <div className="container">
              <div>
                <div style={{ display: "inline" }}>
                  <p>Enter you ID</p>
                </div>
                <Form>
                  <Form.Group className="mb-3" controlId="formBasicEmail">
                    <Form.Control
                      ref={inputRef}
                      type="email"
                      placeholder="Enter ID"
                    />
                  </Form.Group>
                </Form>
              </div>
              {attendance && <div>{attendance}</div>}
              {message && <div>{message}</div>}
              <div>
                <Button variant="secondary" onClick={handleTake}>
                  Take Attendance
                </Button>
                <Button variant="primary" onClick={handleCheck}>
                  Check Attendance
                </Button>
              </div>
            </div>
          </Card.Body>
        </Card>
      </div>
    </div>
  );
}

export default App;
