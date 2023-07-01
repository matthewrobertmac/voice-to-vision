import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import axios from 'axios';
import NavBar from "./NavBar";
import Home from "./Home";
import Profile from "./Profile";
import Text2Texts from "./Text2Texts";
import ImageResults from "./ImageResults";
import ResearchPaper from "./ResearchPaper.js";
import Form from "./Form";
import Audio2Texts from "./Audio2Texts";
import Text2Images from "./Text2Images";
import About from "./About";
import LiveTranscription from "./LiveTranscription";
import Upload from "./Upload";
import UploadOrRecordAudio from "./UploadOrRecordAudio";
import CssBaseline from "@mui/material/CssBaseline";
import Login from "./Login";
import Signup from "./Signup";
import UserDetails from "./UserDetails";

// Create a custom theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#3f51b5',  // Custom primary color
    },
    secondary: {
      main: '#f50057', // Custom secondary color
    },
  },
  typography: {
    fontFamily: 'Roboto',  // Font family (optional)
  },
});

function App() {


  const [data, setData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentUser, setCurrentUser] = useState(null)

  useEffect(() => {
    fetch('/current_session')
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }, [])

  function attemptLogin(userInfo) {
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userInfo)
    })
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }

  function attemptSignup(userInfo) {
    fetch('/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(userInfo)
    })
    .then(res => {
      if (res.ok) {
        res.json()
        .then(user => setCurrentUser(user))
      }
    })
  }

  function logout() {
    setCurrentUser(null)
    fetch('/logout', { method: 'DELETE' })
  }



  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:7000/audio2texts");
        setData(response.data);
        setIsLoading(false);
      } catch (error) {
        setError(error);
        setIsLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (


    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route
            path="/profile"
            render={(props) => <Profile {...props} data={data} />}
          />
          <Route path = '/about' component = {About} />
          <Route path = '/upload' component = {Upload} />
          <Route path = '/form' component = {Form} />
          <Route
            path="/text2texts"
            component={Text2Texts}
          />
          <Route
            path="/audio2texts"
            component={Audio2Texts}
          />
          <Route
            path="/text2images"
            component={Text2Images}
          />
          <Route path="/uploadorrecordaudio" component={UploadOrRecordAudio} />
          <Route path="/research_paper" component={ResearchPaper} />
          <Route path="/imageresults" component={ImageResults} />
          <Route path="/livetranscription" component={LiveTranscription} />
          <Route path="/login" render={(props) => <Login {...props} attemptLogin={attemptLogin} />} />
          <Route path="/signup" render={(props) => <Signup {...props} attemptSignup={attemptSignup} />} />
          <Route path="/userdetails" render={(props) => <UserDetails {...props} currentUser={currentUser} logout={logout} />} />
          <Route path="/logout" render={(props) => <UserDetails {...props} currentUser={currentUser} logout={logout} />} />
        </Switch>
      </BrowserRouter>
    </ThemeProvider>
  );
  }

export default App;

// <div className="App">

// { !currentUser ? <Login attemptLogin={attemptLogin} /> : null }

// { !currentUser ? <Signup attemptSignup={attemptSignup} /> : null }

// { currentUser ? <UserDetails currentUser={currentUser} logout={logout} /> : null }

// <NavBar />
// </div>
// );
// }

// export default App

