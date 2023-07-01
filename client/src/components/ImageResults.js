import React, { useState, useEffect } from "react";
import { Grid, Modal, Backdrop, Fade, Typography, IconButton } from "@mui/material";
import { styled } from "@mui/system";
import { Fullscreen, FullscreenExit, NavigateBefore, NavigateNext } from "@mui/icons-material";

const GalleryContainer = styled(Grid)(({ theme }) => ({
  gap: theme.spacing(2),
}));

const ImageContainer = styled("div")(({ theme }) => ({
  position: "relative",
  cursor: "pointer",
  "& img": {
    width: "100%",
    height: "auto",
    objectFit: "cover",
    borderRadius: theme.shape.borderRadius,
  },
}));

const ModalContent = styled("div")(({ theme }) => ({
  display: "flex",
  flexDirection: "column",
  alignItems: "center",
  width: "60%",
  maxHeight: "80%",
  backgroundColor: theme.palette.background.paper,
  borderRadius: theme.shape.borderRadius,
  boxShadow: theme.shadows[5],
  padding: theme.spacing(2, 4, 3),
  outline: "none",
}));

const FullScreenContainer = styled("div")(({ theme }) => ({
  position: "fixed",
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  display: "flex",
  justifyContent: "center",
  alignItems: "center",
  backgroundColor: theme.palette.background.default,
  zIndex: 9999,
}));

const FullScreenImage = styled("img")(({ theme }) => ({
  maxWidth: "100%",
  maxHeight: "100%",
  borderRadius: theme.shape.borderRadius,
}));

const NavigationContainer = styled("div")(({ theme }) => ({
  position: "absolute",
  top: "50%",
  transform: "translateY(-50%)",
  display: "flex",
  alignItems: "center",
  gap: theme.spacing(2),
}));

const NavigationButton = styled(IconButton)(({ theme }) => ({
  color: theme.palette.common.white,
}));

function ImageResults() {
  const [images, setImages] = useState([]);
  const [selectedImage, setSelectedImage] = useState(null);
  const [isImageLoaded, setIsImageLoaded] = useState(false);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const isFullScreen = () => {
    return document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement;
  };

  const handleFullScreenToggle = () => {
    if (!isFullScreen()) {
      const docElm = document.documentElement;
      if (docElm.requestFullscreen) {
        docElm.requestFullscreen();
      } else if (docElm.mozRequestFullScreen) { // Firefox
        docElm.mozRequestFullScreen();
      } else if (docElm.webkitRequestFullScreen) { // Chrome, Safari and Opera
        docElm.webkitRequestFullScreen();
      } else if (docElm.msRequestFullscreen) { // IE/Edge
        docElm.msRequestFullscreen();
      }
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.mozCancelFullScreen) { // Firefox
        document.mozCancelFullScreen();
      } else if (document.webkitCancelFullScreen) { // Chrome, Safari and Opera
        document.webkitCancelFullScreen();
      } else if (document.msExitFullscreen) { // IE/Edge
        document.msExitFullscreen();
      }
    }
  };

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

  const handleImageError = (image) => {
    // Remove the image from the list if it fails to load
    setImages((prevImages) => prevImages.filter((img) => img.id !== image.id));
  };

  const handlePreviousImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
  };

  const handleNextImage = () => {
    setCurrentImageIndex((prevIndex) => (prevIndex === images.length - 1 ? 0 : prevIndex + 1));
  };

  return (
    <>
      <GalleryContainer container spacing={2}>
        {images.map((image, index) => (
          <Grid item xs={12} sm={6} md={4} key={image.id}>
            {image.image_url && (
              <ImageContainer onClick={() => handleImageClick(image)}>
                <img
                  src={image.image_url}
                  alt={image.source_text}
                  onError={() => handleImageError(image)}
                  onLoad={() => setIsImageLoaded(true)}
                  style={{ display: isImageLoaded ? "block" : "none" }}
                />
                <div>
                  <Typography variant="h6" align="center">
                    {image.source_text}
                  </Typography>
                </div>
              </ImageContainer>
            )}
          </Grid>
        ))}
      </GalleryContainer>

      <Modal
        open={Boolean(selectedImage)}
        onClose={handleCloseModal}
        closeAfterTransition
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 500,
        }}
      >
        <Fade in={Boolean(selectedImage)}>
          <ModalContent>
            {selectedImage && selectedImage.image_url && (
              <>
                <img
                  src={selectedImage.image_url}
                  alt={selectedImage.source_text}
                  style={{ maxWidth: "100%", maxHeight: "80%" }}
                />
                <Typography variant="h6" align="center">
                  {selectedImage.source_text}
                </Typography>
              </>
            )}
          </ModalContent>
        </Fade>
      </Modal>

      {isFullScreen() && (
        <FullScreenContainer>
          <NavigationContainer>
            <NavigationButton onClick={handlePreviousImage}>
              <NavigateBefore />
            </NavigationButton>
            <FullScreenImage src={images[currentImageIndex]?.image_url} alt={images[currentImageIndex]?.source_text} />
            <NavigationButton onClick={handleNextImage}>
              <NavigateNext />
            </NavigationButton>
          </NavigationContainer>
          <IconButton onClick={handleFullScreenToggle}>
            <FullscreenExit />
          </IconButton>
        </FullScreenContainer>
      )}

      <IconButton
        onClick={handleFullScreenToggle}
        sx={{
          position: "fixed",
          bottom: 16,
          right: 16,
          backgroundColor: "rgba(0, 0, 0, 0.6)",
          color: "white",
          "&:hover": {
            backgroundColor: "rgba(0, 0, 0, 0.8)",
          },
        }}
      >
        {isFullScreen() ? <FullscreenExit /> : <Fullscreen />}
      </IconButton>
    </>
  );
}

export default ImageResults;


// import React, { useState, useEffect } from "react";
// import { Grid, Modal, Backdrop, Fade, Typography } from "@mui/material";
// import { styled } from "@mui/system";

// const ImageContainer = styled("div")(({ theme }) => ({
//   cursor: "pointer",
//   "& img": {
//     width: "100%",
//     height: "auto",
//     objectFit: "cover",
//     borderRadius: theme.shape.borderRadius,
//   },
// }));

// const ModalContent = styled("div")(({ theme }) => ({
//   display: "flex",
//   flexDirection: "column",
//   alignItems: "center",
//   width: "60%",
//   maxHeight: "80%",
//   backgroundColor: theme.palette.background.paper,
//   borderRadius: theme.shape.borderRadius,
//   boxShadow: theme.shadows[5],
//   padding: theme.spacing(2, 4, 3),
//   outline: "none",
// }));

// function ImageResults() {
//   const [images, setImages] = useState([]);
//   const [selectedImage, setSelectedImage] = useState(null);

//   useEffect(() => {
//     fetch("/text2images")
//       .then((response) => response.json())
//       .then((data) => setImages(data));
//   }, []);

//   const handleImageClick = (image) => {
//     setSelectedImage(image);
//   };

//   const handleCloseModal = () => {
//     setSelectedImage(null);
//   };

//   const handleImageError = (image) => {
//     // Remove the image from the list if it fails to load
//     setImages((prevImages) => prevImages.filter((img) => img.id !== image.id));
//   };

//   return (
//     <Grid container spacing={2}>
//       {images.map((image) => (
//         <Grid item xs={12} sm={6} md={4} key={image.id}>
//           {image.image_url && (
//             <ImageContainer onClick={() => handleImageClick(image)}>
//               <img
//                 src={image.image_url}
//                 alt={image.source_text}
//                 onError={() => handleImageError(image)}
//               />
//               <div>
//                 <Typography variant="h6" align="center">
//                   {image.source_text}
//                 </Typography>
//               </div>
//             </ImageContainer>
//           )}
//         </Grid>
//       ))}

//       <Modal
//         open={Boolean(selectedImage)}
//         onClose={handleCloseModal}
//         closeAfterTransition
//         BackdropComponent={Backdrop}
//         BackdropProps={{
//           timeout: 500,
//         }}
//       >
//         <Fade in={Boolean(selectedImage)}>
//           <ModalContent>
//             {selectedImage && selectedImage.image_url && (
//               <>
//                 <img
//                   src={selectedImage.image_url}
//                   alt={selectedImage.source_text}
//                   style={{ maxWidth: "100%", maxHeight: "80%" }}
//                 />
//                 <Typography variant="h6" align="center">
//                   {selectedImage.source_text}
//                 </Typography>
//               </>
//             )}
//           </ModalContent>
//         </Fade>
//       </Modal>
//     </Grid>
//   );
// }

// export default ImageResults;

