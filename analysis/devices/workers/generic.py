from analysis.data.data_processors.scatter_data_processor import ScatterDataProcessor
from analysis.data.data_types.generic_scatter import GenericScatterData
from analysis.devices.workers.device_worker import DeviceWorkerCore
from analysis.plotters.scatter_data_plotter import ScatterDataPlotter
from analysis.plotters.histogram_plotter import HistogramPlotter


class Generic(DeviceWorkerCore):

    def __init__(self, device, fileset, plot_type, options):
        # super() delegates method calls to a parent
        super().__init__(device, fileset, plot_type)

        self.x_title = None
        self.y_title = None
        self.legend_title = None
        self.options = options
        self.data_processors = None

        self.set_data_type(GenericScatterData)
        self.set_processor_type(ScatterDataProcessor)

    # FIXME: Option handling is currently a bit of a mess
    def set_options(self, x_title: str, y_title: str, legend_title: str, *args, **kwargs):
        self.x_title = x_title
        self.y_title = y_title
        self.legend_title = legend_title

    def plot(self, title):
        """
        Show the scatter plot
        """
        plotter = ScatterDataPlotter(title, "independent", "dependent")
        plotter.ready_plot(self.data_processors, self.options)
        plotter.set_axes_titles(self.x_title, self.y_title)
        plotter.draw_plot()

    def plot_distribution(self, title):
        """
        Show a histogram
        """
        plotter = HistogramPlotter(title, "dependent")
        plotter.ready_plot(self.data_processors, self.options)
        plotter.set_axes_titles(self.y_title)
        plotter.draw_plot()