from implementations.data.data_processors.scatter_data_processor import ScatterDataProcessor
from implementations.data.data_types.generic_scatter import GenericScatterData
from contracts.device_worker import DeviceWorkerCore
from implementations.plotters.scatter_data_plotter import ScatterDataPlotter
from implementations.plotters.histogram_plotter import HistogramPlotter
from contracts.plotter_options import PlotterOptions


class Generic(DeviceWorkerCore):

    def __init__(self, device, dataspec, plot_type, options: PlotterOptions):
        # super() delegates method calls to a parent
        super().__init__(device, dataspec, plot_type)

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
        plotter.ready_plot(self.data_processors)
        plotter.set_axes_titles(self.options.get_option("x_title"), self.options.get_option("y_title"))
        plotter.draw_plot()

    def plot_distribution(self, title):
        """
        Show a histogram
        """
        plotter = HistogramPlotter(title, "dependent", self.options)
        plotter.ready_plot(self.data_processors)
        plotter.set_axes_titles(self.options.get_option("y_title"))
        plotter.draw_plot()