# Implementing Your Own Device / Module

This page **briefly** explains how to create an implementation module for 
X‑LAB Plotting. Most labs should create their own module by **forking this repo** 
and creating new components.

---

## Overview of What You Must Provide

Every implementation must include:

1. At least one **DataType**  
2. At least one **DataProcessor**  
3. At least one **Plotter**  
4. One **DeviceWorker** tying it all together

Without these, the GUI will raise an error on startup.

---

## Step‑by‑Step Development

### Step 1 — Create Your DataType

Subclass `DataCore` and implement:

- `read_file(self, path)`  
- Populate `self.raw_data`
- Define `self._allowed_observables`

Tips:

- Use pandas for parsing  
- Use header names as observables  
- Keep DataType clean: no physics, no plotting

Use `GenericScatterData` as a template.

---

### Step 2 — Write a DataProcessor

Subclass `DataProcessorCore`:

- Validate required observables  
- Optionally compute derived data (def the methods and add them to the _processing_functions dict)
- Provide structured error messages

Common features:

- Unit conversions  
- Smoothing  
- Calibration corrections  
- Filtering / masking  

Inspect `ScatterDataProcessor` for the simplest possible version.

---

### Step 3 — Add Plotters

Subclass `Plotter`:

- Implement `ready_plot(processors, options)`  
- Implement `draw_plot(ax)`  
- Add GUI-driven options via a `PlotterOptions` subclass

Plotters should only do visualisation, not data manipulation.

---

### Step 4 — Create Your DeviceWorker and Widget

Subclass `DeviceWorkerCore`:

- Complete `__init__()`  
- Provide `plot()`  
- Give your device a name and description

Create a widget with the same base name as the worker python file, but with the `.ui` extension.
Add the new worker class name to `implementations.devices.__init__.py`

```
from . import workers

__all__ = [
    "Generic",
    "NewWorker
]
```

Example:

- `Generic` worker in this repo

---

### Step 5 — Register Your Module with the GUI

The GUI automatically imports everything inside the `implementations` folder.

---

## Recommended Development Pattern

- Fork this repo  
- Add your custom DataTypes first  
- Add processors as needed  
- Add one or more plotters  
- Add your own worker and widget 
- Commit regularly under version control

---

## Learn more

See the main GUI documentation for integration behaviour, logging, error handling,
and UI contract:  
→ [https://allyson-robert.github.io/X-LAB_Plotting_Manager/](https://allyson-robert.github.io/X-LAB_Plotting_Manager/)
