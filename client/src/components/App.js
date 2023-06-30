import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import axios from 'axios';
import NavBar from "./NavBar";
import Home from "./Home";
import Profile from "./Profile";
import Text2Texts from "./Text2Texts";
import Audio2Texts from "./Audio2Texts";
import Text2Images from "./Text2Images";
import About from "./About";
import Upload from "./Upload";
import "./App.css";





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
      </Switch>
    </BrowserRouter>
  );
}

export default App;
