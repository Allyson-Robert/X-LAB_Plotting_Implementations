# Concepts & Architecture

This example implementation is designed to answer a few core questions:

- How should I define a data class that the GUI can load?
- How do processors validate and expose observables?
- How do plotters receive processed data and render figures?
- What is the minimal amount of code required to create a working implementation?

To do that, it uses four main concepts.

## Data Types

**Data type:** a class that encapsulates raw experimental data and exposes it
through a well-defined interface (`DataCore`).

In this example:

- `GenericScatterData` stores the raw x/y values.
- It handles loading from CSV or Excel.
- It exposes observables such as the independent variable, dependent variable,
  and any labels or metadata.

## Data Processors

**Processor:** a class that validates observable requests and prepares data for
plotters.

In this example:

- `ScatterDataProcessor` wraps a `GenericScatterData` instance.
- It checks that requested observables exist and can be returned.
- It delegates unit and data access back to the data type.

More advanced implementations might compute derived observables here.

## Plotters

**Plotter:** a class that turns processed data into a visual representation.

In this example:

- `ScatterDataPlotter` generates simple line / scatter plots.
- `HistogramPlotter` visualises distributions.

Both demonstrate:

- how to receive data from a processor
- how to use `PlotterOptions` to configure the output
- how to produce figures that the GUI can display or export

## Workers (Devices)

**Worker:** a device-specific glue layer that tells the GUI which data types,
processors, and plotters to use.

In this example:

- `Generic` is the worker class.
- It wires together the `GenericScatterData`, `ScatterDataProcessor`, and the
  plotters.
- The GUI discovers this worker and uses it to understand what plots are
  available and how to build them.

When you build your own implementation, you typically:

1. Define one or more data types.
2. Optionally define processors for those data types.
3. Define one or more plotters.
4. Create a worker class that wires all of the above together.
