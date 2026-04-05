# 🐟 Non-Destructive Salmon Spoilage Detection via Computer Vision and Biospeckle Laser Imaging

## 📖 Overview
This project represents a multidisciplinary approach combining **Optical Physics (Photonics)** and **Artificial Intelligence (Computer Vision)** to solve a real-world food science problem. 

By illuminating salmon tissue with a coherent laser source, we can observe microscopic biological and chemical activities (bacterial growth, cellular degradation) as dynamic optical interference patterns, known as **Biospeckle**. This repository provides a conceptual framework and prototype code to process these optical phenomena using Computer Vision algorithms and classify the freshness level of the meat.

## 🌌 The Physics of Photonic Biospeckle (Why it works?)
To truly understand how this system detects spoilage, we must look at the underlying optical physics of **Laser Speckle**:

* **Coherent Scattering:** When a highly coherent light source (like a Laser) illuminates a turbid, optically rough medium such as salmon tissue, the photons penetrate the surface and undergo multiple scattering events.
* **Stochastic Interference:** As these scattered electromagnetic waves exit the tissue and reach the camera sensor, their optical paths differ. The overlapping of these waves causes **constructive interference** (producing bright spots) and **destructive interference** (producing dark spots). This creates a random, granular intensity distribution known as a **Photonic Speckle Pattern**.
* **The "Bio" Dynamics (Time-Varying Phase Shifts):** If you shine a laser on a solid rock, the speckle pattern is completely static. However, biological tissues are dynamic. As the salmon meat degrades, processes such as **intracellular fluid shifts, membrane breakdown, and bacterial motility** act as moving scattering centers.
* **Temporal Scintillation (The "Boiling" Effect):** These microscopic biological movements cause continuous, localized phase shifts (Doppler effects) in the scattered light. As a result, the speckle pattern appears to "boil" or fluctuate over time. 
  * 🐟 **Fresh Sample:** Minimal cellular breakdown; the speckle pattern changes slowly.
  * 🦠 **Spoiled Sample:** High bacterial and fluid activity; the speckle pattern scintillates rapidly.

By analyzing the frequency and variance of this optical "boiling" via Computer Vision, we can mathematically deduce the biological state of the meat without ever touching it.

## 🔬 The Science: Photonics meets AI
The core pipeline of this project bridges the physical and digital worlds:

1. **Photonics (Biospeckle Generation):** When laser light hits the salmon, it scatters. Because the biological tissue is dynamic (micro-movements from bacteria or fluid changes), the scattered light creates a time-varying interference pattern (Speckle). 
2. **Computer Vision (Feature Extraction):** We use **OpenCV** and **NumPy** to analyze the temporal variations of these patterns. By calculating the Time-History Speckle Contrast (THSC), we convert physical optical changes into quantifiable digital matrices.
3. **AI Classification (Decision Making):** The extracted contrast features are fed into a Machine Learning model (e.g., SVM, Random Forest, or CNN) to autonomously classify the salmon into freshness categories (e.g., Fresh, Semi-Fresh, Spoiled).

## ⚙️ Proposed System Pipeline
`[Laser Source] ➔ [Salmon Sample] ➔ [Digital Camera] ➔ [Speckle Contrast Analysis (CV)] ➔ [AI Classifier] ➔ [Freshness Result]`

## 🚀 Current Status
**[Conceptual / Prototype Phase]** This repository currently contains the Opto-digital processing core. It simulates the ingestion of sequential laser speckle images, performs spatial-temporal contrast analysis, and outlines the integration of a Machine Learning classifier for predictive analysis.

## 🛠️ Tech Stack
* **Image Processing:** Python, OpenCV, NumPy
* **AI / Machine Learning:** Scikit-learn (For classification mapping)
* **Data Visualization:** Matplotlib (For rendering Biospeckle Activity Heatmaps)
