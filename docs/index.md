# X‑LAB Plotting – Example Implementations Module

This repository provides a **fully functional reference implementation** for the 
**X‑LAB Plotting Manager**. The GUI cannot run without an implementation module: 
it needs concrete subclasses of the core contracts (`DataCore`, `DataProcessorCore`,
`Plotter`, `DeviceWorkerCore`) to load, process, and plot scientific data.

This module serves two purposes:

1. **A minimal working example** — you can use it immediately to test the GUI.  
2. **A starting point for your own devices** — fork it, rename it, extend it, and
   place it under version control as your lab’s custom implementation.

If you are looking for details about the GUI, refer to the main documentation:  
→ https://allyson-robert.github.io/X-LAB_Plotting_Manager/

## What this implementation provides

- Generic scatter data type  
- CSV/Excel data reading utilities  
- A simple `ScatterDataProcessor`  
- Two example plotters (scatter & histogram)  
- A working `Generic` worker exposing both plotters to the GUI  

## Where to place this implementation

Clone this repository **into the `implementations/` directory** of 
`X-LAB_Plotting_Manager`:

```
X-LAB_Plotting_Manager/
    gui/
    implementations/  ← this repo
```

Once placed here, the GUI will automatically detect and load the module.

## What to read next

- **Getting Started** — run the GUI with this implementation
- **Core Concepts & Contracts** — understand the architecture
- **Example Walkthrough** — see how data → processor → plotter flows
- **Implementing Your Own Module** — create your own device
