# Getting Started with this Implementation

This page shows how to run the X‑LAB Plotting Manager using this example 
implementation, and produce your first plot.

For GUI documentation, see:  
→ [https://allyson-robert.github.io/X-LAB_Plotting_Manager/](https://allyson-robert.github.io/X-LAB_Plotting_Manager/)

---

## 1. Prerequisites

You must already have:

- Python 3.10+
- The main **X‑LAB Plotting Manager** cloned and installed
- This implementation repo cloned into `implementations/`

Directory layout:

```
X-LAB_Plotting_Manager/
    gui/
    implementations/  ← this repo
```

This repository has additional dependencies that must be taken care of.

```bash
pip install -r implementations/requirements-312.txt
```

---

## 2. Launch the GUI

Run:

```
python -m gui.windows.MainWindow
```

On startup, the GUI loads the available implementation modules. 

---

## 3. Load data

1. Click **“New Dataset”**
2. Choose **Files → Add Files**
3. Load any CSV or Excel file containing at least two numerical columns

The `GenericScatterData` reader automatically:

- Detects CSV delimiters
- Reads header names
- Exposes each column as an observable

---

## 4. Select a plot

The GUI automatically lists all plotters compatible with the loaded dataset.
For this module you will see:

- **plot**
- **plot_distribution**

---

## 5. Create your first plot

1. Select *plot* from dropdown
2. Add axis titles
3. Optionally interact with other options
4. Click **Plot**

You should now see your first working plot.

---

## 6. What just happened?

- `GenericScatterData` read your file
- `ScatterDataProcessor` validated observables
- The selected `Plotter` prepared the graphics
- The GUI rendered the result using Matplotlib

To understand these components, continue to  
**Core Concepts & Contracts**.
