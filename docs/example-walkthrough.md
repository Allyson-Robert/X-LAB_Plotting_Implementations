# Example Walkthrough

This section shows a full flow using the example classes in this implementation.

---

## Step 1 — Data: `GenericScatterData`

A simple CSV:

```
1, 10
2, 12
3, 15
```

When loaded:

- Delimiter is auto-detected  
- Raw data stored in a pandas DataFrame 

---

## Step 2 — Processing: `ScatterDataProcessor`

This processor:

- Verifies that X and Y were selected  
- Ensures columns contain numeric data  

No derived quantities in this simple example, but the structure supports them.

---

## Step 3 — Plotting  
### Scatter Plot

`ScatterDataPlotter` implements:

- `ready_plot(processors, options)`  
- Extracts x/y from processor  
- Prepares keyword arguments  
- Applies GUI-selected colours and point styles  
- Returns a callable used by the GUI’s rendering engine

### Histogram

`HistogramPlotter` is even simpler:

- Takes one observable  
- Computes histogram bins  
- Uses Matplotlib to draw the figure

---

## Step 4 — Worker: `Generic`

The `Generic` worker:

- Registers the data type (`GenericScatterData`)
- Registers the processor (`ScatterDataProcessor`)
- Registers available plotters (Scatter + Histogram)
- Provides the GUI entry point and readable name

This worker is what makes the GUI fully functional out of the box.

---

## Summary of the Flow

```
File → GenericScatterData → ScatterDataProcessor → [Plotter] → GUI
```

Next: learn how to **build your own module** using this one as a foundation.
