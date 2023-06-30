import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; // Assuming you have a CSS file for styling your components

function Home() {
  return (
    <div className="home-container">
      <h1 className="title">Voice To Vision</h1>
      <div className="login-container">
        <h2>Login</h2>
        <form className="login-form">
          <div className="form-field">
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" placeholder="Enter Username" required />
          </div>
          <div className="form-field">
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" placeholder="Enter Password" required />
          </div>
          <button className="submit-button" type="submit">Login</button>
        </form>
      </div>
      <div className="project-container">
        <Link to="/form">
          <button className="new-project-button">Start New Project</button>
        </Link>
      </div>
    </div>
  );
}

export default Home;
