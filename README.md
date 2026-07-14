# AI-Based-Early-Glaucoma-Detection-
AI-powered early glaucoma detection using deep learning for OCT retinal image classification
# AI-Based Early Glaucoma Detection System Using OCT Images

## Overview

Glaucoma is one of the leading causes of irreversible blindness worldwide. Early diagnosis is essential to prevent permanent vision loss.

This project presents an AI-based glaucoma detection system using Optical Coherence Tomography (OCT) retinal images. The proposed methodology was designed as a two-stage deep learning pipeline involving retinal layer segmentation followed by glaucoma classification.

> **Note:** Due to project constraints, the final implementation focuses on the classification stage using OCT images.

---

## Features

- Automated glaucoma detection from OCT retinal images
- Deep learning-based image classification
- Binary prediction:
  - Normal
  - Glaucoma
- Image preprocessing for improved model performance
- Model evaluation using accuracy and confusion matrix

---

## Proposed Methodology

### Stage 1 (Proposed)
**RNFL Segmentation**

The original project design included segmentation of the Retinal Nerve Fiber Layer (RNFL) using U-Net to isolate the most relevant retinal region.

Due to technical limitations and project constraints, this stage was not fully integrated into the final implementation.

### Stage 2 (Implemented)
**Glaucoma Classification**

The classification model was trained on OCT retinal images to classify them into:

- Normal
- Glaucoma

using a lightweight CNN architecture.

---

## Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

---

## Dataset

The model was trained using OCT retinal images belonging to two categories:

- Normal
- Glaucoma

*Only sample images are included in this repository. The complete dataset is not uploaded.*

---

## Repository Structure

```
AI-Based-Early-Glaucoma-Detection/
│
├── Classification/
│   ├── classification.ipynb
│   └── outputs/
│
├── Sample_Images/
│
├── Results/
│
├── README.md
│
└── requirements.txt
```

---

## Results

The model successfully classifies OCT retinal images into Normal and Glaucoma categories.

Evaluation metrics include:

- Accuracy
- Loss Curves
- Confusion Matrix

---

## Future Improvements

- Complete RNFL segmentation using U-Net
- Integrate segmentation and classification into a single pipeline
- Deploy the model using Streamlit or Flask
- Improve performance with a larger dataset

---

## Team Members

- Ch. Hemavathi
- S. Suguna
- A. Supriya
- **G. Jyothi**
- G. Pallavi

Project Guide:
**Mrs. G. Gouthami**
Assistant Professor, Department of Computer Science and Engineering

---

## Disclaimer

This repository contains the implementation developed as part of an academic group project. It is intended for educational and research purposes.
