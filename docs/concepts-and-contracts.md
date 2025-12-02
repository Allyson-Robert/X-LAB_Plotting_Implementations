# Core Concepts & Contracts

The X‑LAB Plotting Manager separates responsibilities into four core contracts:

```
DeviceWorker → Plotter ← DataProcessor ← Data
```

Each implementation module must provide **at least one complete chain**.

---

## The Four Contracts

### 1. DataType (subclass of `DataCore`)
Represents a raw measurement dataset.

A DataType must:

- Load data from file(s)
- Define the available **observables**
- Provide access to raw or derived columns

This implementation provides:

- `GenericScatterData` — works with CSV/Excel two-column tabular files

---

### 2. DataProcessor (subclass of `DataProcessorCore`)
Processes or validates data.

A DataProcessor typically:

- Ensures required observables exist  
- Computes derived quantities  
- Prepares data structures for plotting

Provided example:

- `ScatterDataProcessor` — validates X/Y availability, no custom computations are included here.

---

### 3. Plotter (subclass of `Plotter`)
Generates an actual plot.

A Plotter must implement:

- `ready_plot(processors, options)`  
- `draw_plot(ax)`  

This module includes:

- `ScatterDataPlotter`  
- `HistogramPlotter`

Plotters can read custom GUI options via `PlotterOptions`.

---

### 4. DeviceWorker (subclass of `DeviceWorkerCore`)
The **entry point** connecting everything.

Responsibilities:

- Advertise supported DataTypes
- Advertise supported Processors
- Advertise supported Plotters
- Provide metadata (name, description, icons)

This module includes:

- `Generic` — a simple example worker with two plotters

The GUI loads **all DeviceWorkers** at startup and uses them to determine what 
operations are available.

---

## Architectural Flow

1. GUI loads implementation module  
2. Lists available `DeviceWorker` classes  
3. When user selects files:
   - Worker chooses DataTypes  
   - DataTypes produce datasets  
4. Worker attaches appropriate `DataProcessor` instances  
5. GUI lists all compatible `Plotter` classes  
6. Plotter generates the visualisation

---

## Next steps

Read the **Example Walkthrough** to see a complete chain in action.
