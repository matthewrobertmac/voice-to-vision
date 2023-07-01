import React from 'react';
import { Card, CardContent, CardActions, Typography, Button } from '@mui/material';
import styled from '@emotion/styled';

const CustomCard = styled(Card)({
  marginBottom: '20px',
});

const ResearchPapers = () => {
  const papers = [
    {
      title: 'Attention Is All You Need',
      author: 'Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin',
      abstract: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.',
      pdfUrl: 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf',
    },
    {
      title: 'Robust Speech Recognition via Large-Scale Weak Supervision',
      author: 'Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever',
      abstract: 'We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.',
      pdfUrl: 'https://example.com/paper2.pdf',
    },
    {
      title: 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale',
      author: 'Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby',
      abstract: 'While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.',
      pdfUrl: 'https://arxiv.org/pdf/2010.11929.pdf',
    },
  ];

  const handleDownload = (pdfUrl) => {
    window.open(pdfUrl, '_blank');
  };

  return (
    <div className="research-papers">
      {papers.map((paper, index) => (
        <CustomCard key={index}>
          <CardContent>
            <Typography variant="h5" component="div">{paper.title}</Typography>
            <Typography color="textSecondary" gutterBottom>{paper.author}</Typography>
            <Typography variant="body2" component="p">{paper.abstract}</Typography>
          </CardContent>
          <CardActions>
            {paper.pdfUrl ? (
              <Button size="small" color="primary" onClick={() => handleDownload(paper.pdfUrl)}>
                Download PDF
              </Button>
            ) : (
              <Typography color="textSecondary">PDF not available</Typography>
            )}
          </CardActions>
        </CustomCard>
      ))}
    </div>
  );
};

export default ResearchPapers;

// import React from 'react';

// const ResearchPapers = () => {
//   const papers = [
//     {
//       title: 'Attention Is All You Need',
//       author: 'Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin',
//       abstract: 'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.',
//       pdfUrl: 'https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf',
//     },
//     {
//       title: 'Robust Speech Recognition via Large-Scale Weak Supervision',
//       author: 'Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever',
//       abstract: 'We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.',
//       pdfUrl: 'https://example.com/paper2.pdf',
//     },
//     {
//       title: 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale',
//       author: 'Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby',
//       abstract: 'While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components of convolutional networks while keeping their overall structure in place. We show that this reliance on CNNs is not necessary and a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks. When pre-trained on large amounts of data and transferred to multiple mid-sized or small image recognition benchmarks (ImageNet, CIFAR-100, VTAB, etc.), Vision Transformer (ViT) attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train.',
//       pdfUrl: 'https://arxiv.org/pdf/2010.11929.pdf',
//     },
//   ];

//   const handleDownload = (pdfUrl) => {
//     window.open(pdfUrl, '_blank');
//   };

//   return (
//     <div className="research-papers">
//       {papers.map((paper, index) => (
//         <div key={index} className="paper-card">
//           <h2>{paper.title}</h2>
//           <h3 className="mb-2 text-muted">{paper.author}</h3>
//           <p>{paper.abstract}</p>
//           {paper.pdfUrl ? (
//             <button onClick={() => handleDownload(paper.pdfUrl)}>
//               Download PDF
//             </button>
//           ) : (
//             <span className="unavailable-text">PDF not available</span>
//           )}
//         </div>
//       ))}
//     </div>
//   );
// };

// export default ResearchPapers;
