# Mini-Project-Assignment-Smart-Document-Scanner-Quality-Analysis-System

# 📄 Smart Document Scanner & Quality Analysis System

## 📌 Course
Image Processing & Computer Vision  

## 📌 Assignment
Designing a Smart Document Scanner using Python  

## 👤 Student Details
- Name: Swapnil Paroda 
- Roll No: 2301010394  
- Unit: 1  

---

## 🚀 Project Overview

This project simulates a **real-world document scanning system** and analyzes how:

- 📉 Sampling (resolution reduction)
- 🎚️ Quantization (gray level reduction)

affect **document quality, readability, and OCR performance**.

---

## 🎯 Objectives

- Understand image acquisition and preprocessing  
- Convert images to grayscale  
- Analyze resolution impact (sampling)  
- Analyze bit-depth impact (quantization)  
- Compare visual quality degradation  

---

## 🛠️ Technologies Used

- Python 🐍  
- OpenCV  
- NumPy  
- Matplotlib  

---

## 📂 Project Structure
document_scanner/
│── scanner.py
│── document.jpg
│── outputs/
│ ├── original.jpg
│ ├── grayscale.jpg
│ ├── sample_512.jpg
│ ├── sample_256.jpg
│ ├── sample_128.jpg
│ ├── quant_8bit.jpg
│ ├── quant_4bit.jpg
│ ├── quant_2bit.jpg
│ └── comparison.png
│── README.md




---

## 🧪 Sample Inputs

Tested on:
- 📄 Printed document  
- 📑 Scanned PDF page  
- 📷 Camera captured document  

---

## 📊 Results

### 🔹 Sampling (Resolution Analysis)
- **512×512** → Sharp & clear text  
- **256×256** → Slight blur but readable  
- **128×128** → Loss of fine details  

### 🔹 Quantization (Gray Levels)
- **8-bit (256 levels)** → Best quality  
- **4-bit (16 levels)** → Minor banding  
- **2-bit (4 levels)** → Heavy distortion  

---

## 📉 Observations

### 📌 Text Clarity
- High resolution retains sharp edges  
- Low resolution causes blur and pixelation  

### 📌 Readability Degradation
- Reduces significantly at low resolution and low bit depth  

### 📌 OCR Suitability
- ✅ Best: 512×512 + 8-bit  
- ⚠️ Acceptable: 256×256 + 4-bit  
- ❌ Poor: 128×128 + 2-bit  

---
