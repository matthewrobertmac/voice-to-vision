import React from 'react';
import { Card, Button } from 'react-bootstrap';
import { Document, Page, pdfjs } from 'react-pdf';
import 'react-pdf/dist/esm/Page/AnnotationLayer.css';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

const ResearchPapers = ({ papers }) => {
  const handleDownload = (pdfUrl) => {
    window.open(pdfUrl, '_blank');
  };

  return (
    <div className="research-papers">
      {papers.map((paper, index) => (
        <Card key={index} className="paper-card">
          <Card.Body>
            <Card.Title>{paper.title}</Card.Title>
            <Card.Subtitle className="mb-2 text-muted">{paper.author}</Card.Subtitle>
            <Card.Text>{paper.abstract}</Card.Text>
            {paper.pdfUrl ? (
              <Button variant="primary" onClick={() => handleDownload(paper.pdfUrl)}>
                Download PDF
              </Button>
            ) : (
              <span className="unavailable-text">PDF not available</span>
            )}
          </Card.Body>
        </Card>
      ))}
    </div>
  );
};

export default ResearchPapers;
