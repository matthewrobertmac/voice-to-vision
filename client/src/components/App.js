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
        </Switch>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;

// import React, { useState, useEffect } from "react";
// import { BrowserRouter, Route, Switch } from 'react-router-dom';
// import { createTheme, ThemeProvider } from '@mui/material/styles';

// import axios from 'axios';
// import NavBar from "./NavBar";
// import Home from "./Home";
// import Profile from "./Profile";
// import Text2Texts from "./Text2Texts";
// import ImageResults from "./ImageResults";
// import ResearchPaper from "./ResearchPaper.js";
// import Form from "./Form";
// import Audio2Texts from "./Audio2Texts";
// import Text2Images from "./Text2Images";
// import About from "./About";
// import Upload from "./Upload";
// import UploadOrRecordAudio from "./UploadOrRecordAudio";
// import "./App.css";

// const theme = createTheme();

// function App() {
//   const [data, setData] = useState([]);
//   const [isLoading, setIsLoading] = useState(true);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const response = await axios.get("http://localhost:7000/audio2texts");
//         setData(response.data);
//         setIsLoading(false);
//       } catch (error) {
//         setError(error);
//         setIsLoading(false);
//       }
//     };

//     fetchData();
//   }, []);

//   if (isLoading) {
//     return <div>Loading...</div>;
//   }

//   if (error) {
//     return <div>Error: {error.message}</div>;
//   }

//   return (
//     <ThemeProvider theme={theme}>
//     <BrowserRouter>
//       <NavBar />
//       <Switch>
//         <Route path="/" exact component={Home} />
//         <Route
//           path="/profile"
//           render={(props) => <Profile {...props} data={data} />}
//         />
//         <Route path = '/about' component = {About} />
//         <Route path = '/upload' component = {Upload} />
//         <Route path = '/form' component = {Form} />
//         <Route
//           path="/text2texts"
//           component={Text2Texts}
//         />
//         <Route
//           path="/audio2texts"
//           component={Audio2Texts}
//         />
        
//         <Route
//           path="/text2images"
//           component={Text2Images}
//         />
//         <Route path="/uploadorrecordaudio" component={UploadOrRecordAudio} />
//         <Route path="/research_paper" component={ResearchPaper} />
//         <Route path="/imageresults" component={ImageResults} />
        
//       </Switch>
//     </BrowserRouter>
//     </ThemeProvider>
//   );
// }

// export default App;
