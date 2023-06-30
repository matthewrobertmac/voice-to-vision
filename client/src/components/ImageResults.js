import React, { useState, useEffect } from "react";
import './ImageResults.css';

function ImageResults() {
  const [images, setImages] = useState([]);
  const [selectedImage, setSelectedImage] = useState(null);

  useEffect(() => {
    fetch("/text2images")
      .then((response) => response.json())
      .then((data) => setImages(data));
  }, []);

  const handleImageClick = (image) => {
    setSelectedImage(image);
  };

  const handleCloseModal = () => {
    setSelectedImage(null);
  };

  return (
    <div className="image-grid">
      {images.map((image) => (
        <div 
          className="image-container" 
          key={image.id} 
          onClick={() => handleImageClick(image)}
        >
          <img className="image-item" src={image.image_url} alt={image.source_text} />
          <div className="image-info">
            <h3>{image.source_text}</h3>
          </div>
        </div>
      ))}

      {selectedImage && (
        <div className="modal" onClick={handleCloseModal}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <img className="modal-image" src={selectedImage.image_url} alt={selectedImage.source_text} />
            <h3>{selectedImage.source_text}</h3>
          </div>
        </div>
      )}
    </div>
  );
}

export default ImageResults;
