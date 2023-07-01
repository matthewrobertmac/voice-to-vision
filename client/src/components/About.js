
import React from 'react';
import { Link } from 'react-router-dom';
import './About.css';

function About() {
  return (
    <div className="about-container">
      <h1 className="about-heading">Welcome to Voice-to-Vision</h1>
      <div className="about-content">
        <p className="about-summary">
          Voice-to-Vision is an innovative AI art application that leverages cutting-edge technologies to transform spoken or sung text into stunning visual artworks.
        </p>
        <p className="about-summary">
          Our application utilizes advanced AI models such as OpenAI Whisper, GPT-3.5, and DALL-E 2, offering a unique creative experience for users.
        </p>
        <div className="about-section">
          <h2 className="about-section-heading">AI Model Workflow</h2>
          <p className="about-section-summary">
            Voice-to-Vision employs a sophisticated workflow that involves three main AI models: Speech-to-Text, Text-to-Text, and Text-to-Image.
          </p>
          <p className="about-section-summary">
            The Speech-to-Text model, powered by OpenAI Whisper, transcribes user speech input into text, supporting over 80 languages and providing accessibility to a wider audience.
          </p>
          <p className="about-section-summary">
            The Text-to-Text model, using OpenAI GPT-3.5, enhances the transcribed text by generating refined prompts. This enhances the creativity and expressiveness of the generated visual art.
          </p>
          <p className="about-section-summary">
            The Text-to-Image model, powered by OpenAI DALL-E 2, transforms the refined prompts into stunning visual artworks. It generates multiple images based on the prompts, opening up possibilities for unique artistic creations.
          </p>
        </div>
        <div className="about-section">
          <h2 className="about-section-heading">Use Cases</h2>
          <p className="about-section-summary">
            Voice-to-Vision has a wide range of applications, including:
          </p>
          <ul className="about-use-cases">
            <li>Artistic Expression: Artists can transform their spoken or sung ideas into visually captivating artworks, exploring new dimensions of creativity.</li>
            <li>Interactive Installations: Voice-to-Vision can be used in interactive art installations, allowing audiences to participate in the creation of unique artworks using their voices.</li>
            <li>Multimedia Productions: Film directors, game developers, and multimedia creators can generate visually striking scenes and characters by combining voice inputs with AI-generated images.</li>
          </ul>
        </div>
        <div className="about-section">
          <h2 className="about-section-heading">Join the Voice-to-Vision Community</h2>
          <p className="about-section-summary">
            We invite you to join the Voice-to-Vision community and unleash your creative potential. Start creating AI artworks from your voice today!
          </p>
          <Link to="/signup" className="about-button">Sign Up</Link>
        </div>
      </div>
      <Link to="/" className="about-back-link">Go back to Home</Link>
    </div>
  );
}

export default About;
