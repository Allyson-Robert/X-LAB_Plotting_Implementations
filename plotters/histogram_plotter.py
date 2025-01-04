from analysis.data.data_processors.data_processors import DataProcessor
from utils.plot_preppers.scatter_prep import scatter_prepper
from utils.plot_preppers.export_to_svg import get_svg_config
from analysis.plotters.plotter_options import PlotterOptions
from analysis.plotters.plotter import Plotter
import plotly.graph_objects as go
import plotly.colors


class HistogramPlotter(Plotter):
    def __init__(self, title, observable: str, options: PlotterOptions):
        self.titles_set = None
        self.title = title
        self.fig = go.Figure()
        self.observable = observable

        self.data_processors = None

        # This is very similar to ScatterPlotter
        expected_options = ["y_title", "legend_title", "presentation", "time_evolved"]
        if options.is_instance_valid(expected_options):
            self.options = options
        self.options.add_option(label="colourscale", value=plotly.colors.get_colorscale("Viridis"))

    def ready_plot(self, data_processors: dict[str, DataProcessor]):
        self.fig = scatter_prepper(self.fig)
        self.fig.update_layout(
            title={'text': self.title},
            legend_title=self.options.get_option("legend_title")
        )
        self.data_processors = data_processors

    def set_axes_titles(self, x_title):
        self.fig.update_layout(
            xaxis_title=x_title,
        )
        self.titles_set = True

    def draw_plot(self):
        for lbl in self.data_processors:
            processor = self.data_processors[lbl]

            self.fig.add_trace(
                go.Histogram(
                    x=processor.get_data(self.observable),
                    name=processor.get_data("label")
                )
            )

        # Grab axis titles from last processor if they have not yet been externally set
        if not self.titles_set:
            self.set_axes_titles(
                processor.get_units(self.x_observable)
            )
        self.fig.update_layout(
            yaxis_title="$Counts$",
        )
        self.fig.show(config=get_svg_config())
