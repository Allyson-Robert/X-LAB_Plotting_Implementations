# X-LAB Plotting Example

This repository provides a **minimal but complete example
implementation** for the **X-LAB Plotting framework**.\
It demonstrates how to define data types, processors, plotters, and
device workers that integrate cleanly with the X-LAB GUI.

In the most general sense, this example shows how to implement the 
following class/methods structure:

![X-LAB Implementation Structure](docs/Contracts.png)

## 📘 What This Example Includes

### 1. Minimal Data Type

**`GenericScatterData`**\
A simple two-column (x/y) dataset container supporting CSV and Excel
files.\
Use it as a reference for creating your own loadable data types via the
`DataCore` interface.

### 2. Simple Data Processor

A lightweight processor that performs basic transformations on the
sample dataset.\
Shows how to implement and register processors within the framework.

### 3. Example Plotters

A small set of plotters illustrating:

-   use of the core `Plotter` interface\
-   consuming the processed data\
-   exposing configuration through `PlotterOptions`

These serve as templates for creating custom visual components.

### 4. Device Worker

**`Generic` Worker**\
Wires together the data type, processor, and plotters.\
This class demonstrates how the main X-LAB GUI discovers and loads
device-specific modules.

## 📂 Documentation

Full documentation is available in the `docs/` folder:

- Overview: [index.md](docs/index.md)
- Concept: [concepts-and-architecture.md](docs/concepts-and-architecture.md)
- Using and Extending: [using-and-extending.md](docs/using-and-extending.md)
- What this Example Provides: [what-this-example-provides.md](docs/what-this-example-provides.md)

## 🚀 Purpose

This example serves as a **starting point** for developers building new
device integrations or custom plotting capabilities within the X-LAB
ecosystem. Feel free to copy, adapt, and extend the provided components.
