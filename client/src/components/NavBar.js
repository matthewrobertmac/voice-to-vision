import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <AppBar position="static" style={{ backgroundColor: 'rgba(0, 0, 255, 0.3)', boxShadow: 'none' }}>
      <Toolbar>
        <Box sx={{ display: 'flex', flexGrow: 1, justifyContent: 'space-between', alignItems: 'center' }}>
          <Typography variant="h6" style={{ fontFamily: 'Arial, sans-serif' }}>
            Voice-to-Vision
          </Typography>
          <Box sx={{ '& > :not(style)': { m: 1, textTransform: 'none', fontFamily: 'Verdana, sans-serif' } }}>
            <Button variant="text" color="inherit" component={Link} to="/" 
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Home
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/profile"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Profile
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/about"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              About
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/upload"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Upload
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/text2texts"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Text to Texts
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/audio2texts"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Audio to Texts
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/text2images"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Text to Images
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/uploadorrecordaudio"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Upload or Record Audio
            </Button>

            <Button variant="text" color="inherit" component={Link} to="/research_paper"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Research Paper
            </Button>
            <Button variant="text" color="inherit" component={Link} to="/imageresults"
              sx={{ '&:hover': { backgroundColor: 'rgba(0, 0, 255, 0.2)' } }}>
              Image Results
            </Button>
          </Box>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export default NavBar;

// import React from 'react';
// import { NavLink } from 'react-router-dom';
// import './NavBar.css';

// function NavBar() {
//   return (
//     <nav className="navbar">
//       <h3 className="navbar-header">User-Related</h3>
//       <div className="navbar-item">
//         <NavLink to="/profile" activeClassName="navbar-link-active">Profile</NavLink>
//       </div>

//       <h3 className="navbar-header">Media-Related</h3>
//       <div className="navbar-item">
//         <NavLink to="/audio2texts" activeClassName="navbar-link-active">Audio to Text</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/text2texts" activeClassName="navbar-link-active">Text to Text</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/text2images" activeClassName="navbar-link-active">Text to Images</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/upload" activeClassName="navbar-link-active">Upload MP3</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/upload-or-record-audio" activeClassName="navbar-link-active">Upload or Record Audio</NavLink>
//       </div>

//       <h3 className="navbar-header">Miscellaneous</h3>
//       <div className="navbar-item">
//         <NavLink exact to="/" activeClassName="navbar-link-active">Home</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/about" activeClassName="navbar-link-active">About</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/form" activeClassName="navbar-link-active">Form</NavLink>
//       </div>
//       <div className="navbar-item">
//         <NavLink to="/research_paper" activeClassName="navbar-link-active">Research Paper</NavLink>
//       </div>
//     </nav>
//   );
// }

// export default NavBar;
