import React from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css'; // Assuming you have a CSS file for styling your components

function NavBar() {
  return (
    <nav className="navbar">
      <div className="navbar-item">
        <NavLink exact to="/" activeClassName="navbar-link-active">Home</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/uploadmp3" activeClassName="navbar-link-active">Upload MP3</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/audio2texts" activeClassName="navbar-link-active">Audio2Texts</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/text2texts" activeClassName="navbar-link-active">Text2Texts</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/text2images" activeClassName="navbar-link-active">Text2Images</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/profile" activeClassName="navbar-link-active">Profile</NavLink>
      </div>
    </nav>
  );
}

export default NavBar;