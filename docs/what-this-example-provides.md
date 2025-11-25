# What This Example Provides

This implementation demonstrates several minimal but complete building blocks
for X-LAB Plotting.

## 1. A Minimal Data Type

**`GenericScatterData`**  
A simple two-column x/y dataset container supporting Excel or CSV inputs,
implemented using the core `DataCore` interface.

Use this as a template for defining your own data classes that the X-LAB GUI
can load and inspect.

## 2. A Simple Data Processor

**`ScatterDataProcessor`**  
A lightweight processor that validates requested observables and delegates raw
data access to the data type.

It shows how processors:

- expose available observables
- validate requests for observables
- hand data off to plotters

## 3. Example Plotters

- **`ScatterDataPlotter`** — for basic line or scatter-style plots  
- **`HistogramPlotter`** — for quick distribution visualisations

These plotters demonstrate how to:

- integrate with the core `Plotter` interface
- consume processed data from a processor
- expose configuration via `PlotterOptions`

## 4. A Device Worker

**`Generic`**  
A concrete worker that wires the example data type, processor, and plotters
together.

This class shows **how the main GUI discovers and uses implementations** and is
the best starting point when wiring up your own device-specific worker.
