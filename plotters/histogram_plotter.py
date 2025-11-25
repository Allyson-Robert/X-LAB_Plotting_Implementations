from contracts.data_processors import DataProcessor
from implementations.utils.plot_preppers.scatter_prep import scatter_prepper
from implementations.utils.plot_preppers.export_to_svg import get_svg_config
from contracts.plotter_options import PlotterOptions
from contracts.plotter import Plotter
import plotly.graph_objects as go
import plotly.colors
from utils.logging import decorate_class_with_logging, DEBUG_PLOTTER


@decorate_class_with_logging(log_level=DEBUG_PLOTTER)
class HistogramPlotter(Plotter):
    """
    HistogramPlotter
    ================

    A Plotly-based histogram plotter for processed observables. This class
    implements the `Plotter` interface and visualises a single observable
    from one or more `DataProcessor` instances as overlaid histograms.

    Overview
    --------
    `HistogramPlotter`:

    - Accepts a dictionary of `DataProcessor` objects keyed by label
    - Plots a histogram for the chosen observable from each processor
    - Uses `PlotterOptions` to configure axis titles, legend title,
      and other layout options
    - Adds a default colourscale to the options for consistent styling

    The x-axis represents the selected observable, while the y-axis shows
    the counts in each histogram bin.

    Usage Notes
    -----------
    Call `ready_plot` with the data processors and options to configure the
    figure, then call `set_axes_titles` to customise axis labels if desired.
    Finally, call `draw_plot` to render the histogram and show it using the
    SVG export configuration.
    """

    def __init__(self, title, observable: str, options: PlotterOptions):
        self.titles_set = None
        self.title = title
        self.fig = go.Figure()
        self.observable = observable

        self.data_processors = None

        # This is very similar to ScatterPlotter
        expected_options = ["y_title", "legend_title", "presentation", "time_evolved"]
        if options.has_options(expected_options):
            self.options = options
        self.options.add_option(label="colourscale", value=plotly.colors.get_colorscale("Viridis"))

    def ready_plot(self, data_processors: dict[str, DataProcessor], options: PlotterOptions):
        self.fig = scatter_prepper(self.fig)
        self.fig.update_layout(
            title={'text': self.title},
            legend_title=options.get_option("legend_title")
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
