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
        <NavLink to="/upload" activeClassName="navbar-link-active">Upload MP3</NavLink>
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
      <div className="navbar-item">
        <NavLink to="/about" activeClassName="navbar-link-active">About</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/logout" activeClassName="navbar-link-active">Logout</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/login" activeClassName="navbar-link-active">Login</NavLink>
      </div>
      <div className='navbar-item'>
        <NavLink to="/signup" activeClassName="navbar-link-active">Signup</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/form" activeClassName="navbar-link-active">Form</NavLink>
      </div>
      <div className="navbar-item">
        <NavLink to="/upload-or-record-audio" activeClassName="navbar-link-active">Upload or Record Audio</NavLink>
      </div>
    </nav>
  );
}

export default NavBar;