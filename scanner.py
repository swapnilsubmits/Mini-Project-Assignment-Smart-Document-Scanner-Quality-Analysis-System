"""
Name: YOUR NAME
Roll No: YOUR ROLL NO
Course: Image Processing & Computer Vision
Unit: 1
Assignment Title: Smart Document Scanner & Quality Analysis System
Date: 
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print("=== Smart Document Scanner & Quality Analysis System ===")

# Create output folder
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------
# Task 2: Image Acquisition
# -------------------------------

# Load image (change filename)
image_path = "document.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found!")
    exit()

# Resize
img = cv2.resize(img, (512, 512))

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("outputs/original.jpg", img)
cv2.imwrite("outputs/grayscale.jpg", gray)

# -------------------------------
# Task 3: Sampling
# -------------------------------

def sample_image(image, size):
    small = cv2.resize(image, size)
    upscaled = cv2.resize(small, (512, 512))
    return upscaled

high_res = gray.copy()  # 512x512
med_res = sample_image(gray, (256, 256))
low_res = sample_image(gray, (128, 128))

cv2.imwrite("outputs/sample_512.jpg", high_res)
cv2.imwrite("outputs/sample_256.jpg", med_res)
cv2.imwrite("outputs/sample_128.jpg", low_res)

# -------------------------------
# Task 4: Quantization
# -------------------------------

def quantize(image, levels):
    factor = 256 // levels
    quantized = (image // factor) * factor
    return quantized

q_8bit = quantize(gray, 256)
q_4bit = quantize(gray, 16)
q_2bit = quantize(gray, 4)

cv2.imwrite("outputs/quant_8bit.jpg", q_8bit)
cv2.imwrite("outputs/quant_4bit.jpg", q_4bit)
cv2.imwrite("outputs/quant_2bit.jpg", q_2bit)

# -------------------------------
# Task 5: Display Comparison
# -------------------------------

titles = [
    "Original", "Grayscale",
    "512x512", "256x256", "128x128",
    "8-bit", "4-bit", "2-bit"
]

images = [
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB), gray,
    high_res, med_res, low_res,
    q_8bit, q_4bit, q_2bit
]

plt.figure(figsize=(12, 8))

for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.savefig("outputs/comparison.png")
plt.show()

# -------------------------------
# Observations
# -------------------------------

print("\n=== Observations ===")

print("1. Sampling Effects:")
print("- 512x512: Clear text and sharp edges")
print("- 256x256: Slight blur, still readable")
print("- 128x128: Significant loss of detail")

print("\n2. Quantization Effects:")
print("- 8-bit: No visible loss")
print("- 4-bit: Minor banding")
print("- 2-bit: Heavy distortion, poor readability")

print("\n3. OCR Suitability:")
print("- Best: 512x512 & 8-bit")
print("- Acceptable: 256x256 & 4-bit")
print("- Poor: 128x128 & 2-bit")