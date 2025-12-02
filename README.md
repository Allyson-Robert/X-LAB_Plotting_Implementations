# X-LAB Plotting Manager

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-lightgrey)
![Licence](https://img.shields.io/badge/license-AGPL--3.0-blue)
![Status](https://img.shields.io/badge/status-active-success)
[![DOI](https://zenodo.org/badge/688853127.svg)](https://doi.org/10.5281/zenodo.17792620)


The **X-LAB Plotting Manager** is a desktop application for organising scientific datasets and producing publication‑ready plots using clean, reusable modules.

![MainWindow](docs/images/MainWindow.png)
---

## 🚀 Quick Start

1. **Install Python 3.10+**  
2. **Clone this repository:**  
   ```bash
   git clone https://github.com/Allyson-Robert/X-LAB_Plotting_Manager.git
   ```
3. **Create a virtual environment & install dependencies:**  
   ```bash
   cd X-LAB_Plotting_Manager
   python -m venv .venv
   source .venv/bin/activate       # Windows: .venv\Scripts\activate
   pip install -r requirements-312.txt
   ```
4. **Add an implementation package** (required for the GUI to run):  
   ```bash
   git clone https://github.com/Allyson-Robert/X-LAB_Plotting_Manager_Implementations.git implementations/
   pip install -r implementations/requirements-312.txt
   ```
   A short introduction to implementations and how to write your own is available in the [documentation](https://allyson-robert.github.io/X-LAB_Plotting_Manager/).


5. **Launch the application:**  
   ```bash
   python -m gui.windows.MainWindow
   ```
---

## 📁 Creating a Dataset

Use **File → Create Set** in the menu bar to define a dataset from your raw files and metadata.

![DataCreationWindow](docs/images/DataCreationWindow.png)

Full details on datasets and the workflow are explained in the documentation.

---

## 📚 Documentation

Full documentation:  
**https://allyson-robert.github.io/X-LAB_Plotting_Manager/**

The docs cover:

- installation  
- implementations  
- creating datasets  
- generating plots  
- troubleshooting  

---

## 📄 License

This project is built using PyQt5 and licensed under the **AGPL**. 
See the included `LICENSE` file for full terms.

---

## Known Issues

A PyQt5 deprecation warning may appear under Python 3.10. 
It is harmless and can be ignored.

