# X-LAB Plotting – Generic Example Implementation

Welcome to the **Generic Example Implementation** for **X-LAB Plotting**.  
This repository provides a minimal, fully functional reference implementation that demonstrates how to structure data types, processors, and plotters so they can be discovered and used by the main X-LAB Plotting Manager GUI.

The goal of this example is twofold:

1. **Provide a clean, lightweight reference** for developers who want to implement their own custom data handling and plotting logic.
2. **Serve as a template** illustrating the contracts and interfaces required by the main application.

This repository **only** contains the *example* implementation modules.  
It is intended to be read, modified, copied, or replaced when creating your own plotting modules.

---

## What This Example Provides

This implementation demonstrates:

### **1. A Minimal Data Type**
`GenericScatterData`  
A simple two-column x/y dataset container supporting Excel or CSV inputs, implemented using the core `DataCore` interface.

### **2. A Simple Data Processor**
`ScatterDataProcessor`  
A lightweight processor that validates requested observables and delegates raw data access to the data type.

### **3. Example Plotters**
- `ScatterDataPlotter` — for basic line or scatter-style plots  
- `HistogramPlotter` — for quick distribution visualisations

These plotters serve as clear examples of how to integrate with the core `Plotter` interface and use `PlotterOptions` to configure their output.

### **4. A Device Worker**
`Generic`  
A concrete worker wiring the example data type, processor, and plotters together.  
This shows **exactly how the main GUI discovers and uses implementations**.

---

## Why This Example Exists

The generic example answers key questions for developers:

- *How should I define a data class that the GUI can load?*  
- *How do processors validate and expose observables?*  
- *How do plotters receive processed data and render figures?*  
- *What is the minimal amount of code required to create a working implementation?*

This repository acts as the authoritative reference for building your own custom modules.

---

## How to Use This Repository/Extend This Example

This example repo is meant to be **cloned inside** the main GUI project directory:

```
X-LAB_Plotting_Manager/
    gui/
    implementations/ ← this repo
```

Once cloned as *implementations*, the main GUI can automatically detect and load the example implementation without installing it as a package.
You can modify and/or add data types, data processors, plotters and workers as needed following the contracts defined in the main repository.
Workers have authority over which types of plots are available for a given device as well as which classes are used to read and analyse/process the data needed to produce those plots.
