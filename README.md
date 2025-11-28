# X-LAB Plotting Example Implementations
 
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/example-implementation-success)

This repository provides a **minimal, fully functional implementation package** for the **X-LAB Plotting Manager**.  
It serves as a **reference template** demonstrating how to implement custom:

- Data types  
- Data processors  
- Plotters  
- Device workers  

All components comply with the X-LAB contracts and integrate cleanly with the main GUI.
For the main repository containing the GUI, visit the [X-LAB Plotting Manager Repository](https://github.com/Allyson-Robert/X-LAB_Plotting_Manager) or the corresponding documentation on the [X-LAB Plotting Manager GitHub Pages](https://Allyson-Robert.github.io/X-LAB_Plotting_Manager_implementations/).

---

## 📦 Installation

> 🔗 **Important:** This repository is meant to live inside the `implementations/` folder of the main **X-LAB Plotting Manager** project.

1. Clone the main GUI repository (if you haven’t already):

   ```bash
   git clone https://github.com/Allyson-Robert/X-LAB_Plotting_Manager.git
   cd X-LAB_Plotting_Manager
   ```

2. Clone this example into the `implementations/` folder:

   ```bash
   git clone https://github.com/Allyson-Robert/X-LAB_Plotting_Manager_Implementations.git implementations/
   ```

3. (Recommended) Activate the same virtual environment you use for the main GUI, then install the implementation dependencies, for example:

   ```bash
   # inside the X-LAB_Plotting_Manager root
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -r implementations/requirements-312.txt
   ```

Once this repository is present under `implementations/` and its dependencies are installed,  
the X-LAB GUI will detect and use these example implementations automatically.

---

## ✨ What This Example Provides

### 📁 1. Minimal Data Type  
**`GenericScatterData`**

A simple two-column (`x`, `y`) data container supporting CSV and Excel input.  
Use it as a model for creating your own loadable data types based on the `DataCore` contract.

---

### ⚙️ 2. Example Data Processor  
A lightweight processor showcasing:

- How to declare derived observables  
- On-demand computation using `DataProcessorCore`  
- Correct integration with the X-LAB pipeline  

This is a minimal but correct example of a processor implementation.

---

### 📊 3. Plotter Implementations  

A small set of Plotly-based plotters demonstrating:

- Usage of the core `Plotter` interface  
- Accessing processed data  
- Exposing adjustable configuration through `PlotterOptions`  

These templates can be extended into more advanced visualizations.

---

### 🔧 4. Device Worker  

**`GenericDeviceWorker`** coordinates:

- The data class  
- The processor  
- The plotters  

This class shows how the X-LAB GUI locates and interacts with device-specific workers.  
Your own implementation package should provide at least one worker class like this.

---

## 🧩 Architecture Overview

This example follows the same structure all X-LAB implementation packages use:

![X-LAB Implementation Structure](docs/Contracts.png)

Your own implementation can follow the same pattern—simply place it in an `implementations/` folder inside the main X-LAB GUI project.

---

## 📚 Documentation

Full documentation is included in the `docs/` directory:

- Overview: [docs/index.md](docs/index.md)  
- Concepts & Architecture: [docs/concepts-and-architecture.md](docs/concepts-and-architecture.md)  
- Using & Extending: [docs/using-and-extending.md](docs/using-and-extending.md)  
- Explanation of this example: [docs/what-this-example-provides.md](docs/what-this-example-provides.md)

### View pre-built documentation locally

```bash
python -m http.server -d site 8000
```

Then open: <http://localhost:8000>

---

## 🚀 Purpose

This repository provides a **clean starting point** for developing:

- New device integrations  
- Custom data readers  
- Custom processors  
- Custom plotters  

Feel free to adapt, expand, and repurpose this example as the foundation of your own implementation module.

---

## 🤝 Contributing

Contributions that:

- Improve clarity  
- Add new example implementations  
- Expand documentation  

are very welcome!

### To contribute:

1. Fork this repository  
2. Create a feature branch  
3. Add your changes  
4. Submit a pull request  

Please follow the X-LAB contract architecture and file structure to ensure compatibility.