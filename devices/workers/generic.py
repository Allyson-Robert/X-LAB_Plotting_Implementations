from implementations.data.data_processors.scatter_data_processor import ScatterDataProcessor
from implementations.data.data_types.generic_scatter import GenericScatterData
from contracts.device_worker import DeviceWorkerCore
from implementations.plotters.scatter_data_plotter import ScatterDataPlotter
from implementations.plotters.histogram_plotter import HistogramPlotter
from contracts.plotter_options import PlotterOptions


class Generic(DeviceWorkerCore):
    """
    Generic
    =======

    Device worker for generic scatter-type datasets. This class extends
    `DeviceWorkerCore` and wires together the data type, processor, and
    plotters for simple scatter and histogram visualisations.

    Overview
    --------
    `Generic` configures the worker to use:

    - `GenericScatterData` as the underlying data container
    - `ScatterDataProcessor` to access and validate observables
    - `ScatterDataPlotter` for x–y scatter plots
    - `HistogramPlotter` for value distributions

    It uses a `PlotterOptions` instance to control plot appearance, axis
    titles, and legend labels.

    Usage Notes
    -----------
    Use `plot` to generate a standard scatter plot of the *independent*
    versus *dependent* observable, and `plot_distribution` to generate
    a histogram of the *dependent* observable across all loaded datasets.
    """

    def __init__(self, device, dataspec, plot_type, options: PlotterOptions):
        # super() delegates method calls to a parent
        super().__init__(device, dataspec, plot_type, options)

        self.x_title = None
        self.y_title = None
        self.legend_title = None
        self.options = options
        self.data_processors = None

        self.set_data_type(GenericScatterData)
        self.set_processor_type(ScatterDataProcessor)

    def plot(self, title):
        """
        Show the scatter plot
        """
        plotter = ScatterDataPlotter(title, "independent", "dependent", self.options)
        plotter.ready_plot(self.data_processors, options=self.options)
        plotter.set_axes_titles(self.options.get_option("x_title"), self.options.get_option("y_title"))
        plotter.draw_plot()

    def plot_distribution(self, title):
        """
        Show a histogram
        """
        plotter = HistogramPlotter(title, "dependent", self.options)
        plotter.ready_plot(self.data_processors, options=self.options)
        plotter.set_axes_titles(self.options.get_option("y_title"))
        plotter.draw_plot()