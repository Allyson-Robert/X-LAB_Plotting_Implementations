from contracts.data_processors import DataProcessor
from utils.plot_preppers.scatter_prep import scatter_prepper
from utils.plot_preppers.export_to_svg import get_svg_config
from contracts.plotter_options import PlotterOptions
from contracts.plotter import Plotter
from implementations.utils.get_colour import get_colour
import plotly.graph_objects as go
import plotly.colors


class ScatterDataPlotter(Plotter):
    """
    ScatterDataPlotter
    ==================

    A Plotly-based line scatter plotter for generic x–y datasets. This class
    implements the `Plotter` interface and draws one or more traces from
    `DataProcessor` instances.

    Overview
    --------
    `ScatterDataPlotter`:

    - Plots a chosen x observable versus a chosen y observable
    - Accepts a dictionary of `DataProcessor` objects keyed by label
    - Uses `PlotterOptions` to set axis titles, legend title, and line
      styling
    - Supports a "presentation" mode with thicker lines
    - Supports "time_evolved" plots by switching to a different colourscale

    Each trace is assigned a colour from the configured colourscale based on
    its index, and is plotted as a continuous line.

    Usage Notes
    -----------
    Call `ready_plot` to prepare the figure and configure options, then
    optionally call `set_axes_titles` to override axis labels. Finally,
    call `draw_plot` to add all traces and display the figure using the SVG
    export configuration.
    """

    def __init__(self, title, x_observable: str, y_observable: str, options: PlotterOptions):
        self.title = title
        self.fig = go.Figure()
        self.x_observable = x_observable
        self.y_observable = y_observable

        self.data_processors = None
        self.titles_set = False
        self.sort_x_array = False

        expected_options = ["x_title", "y_title", "legend_title", "presentation", "time_evolved"]
        if options.has_options(expected_options):
            self.options = options
        options.add_option(label="colourscale", value=plotly.colors.get_colorscale("Viridis"))

    def ready_plot(self, data_processors: dict[str, DataProcessor], options: PlotterOptions):
        self.fig = scatter_prepper(self.fig)
        self.fig.update_layout(
            title={'text': self.title},
            legend_title=self.options.get_option("legend_title"),
        )
        self.data_processors = data_processors

        # Line should be thicker for presentations
        if self.options.get_option("presentation"):
            self.options.add_option(label="line", value={"width": 5})
        else:
            self.options.add_option(label="line", value={"width": 1})

        # Set colourscale for the continuous time evolved data
        if self.options.get_option("time_evolved"):
            self.options.add_option(label="colourscale", value=plotly.colors.get_colorscale("Magenta"))

    # Gets called by draw_plot to populate with data units if not manually set
    def set_axes_titles(self, x_title, y_title):
        self.fig.update_layout(
            xaxis_title=x_title,
            yaxis_title=y_title,
        )
        self.titles_set = True

    def draw_plot(self, *args, **kwargs):
        # FEATURE REQUEST: Draw plots with errors
        for index, lbl in enumerate(self.data_processors):
            # Set line colour for current line
            line = self.options.get_option("line")
            line["color"] = get_colour(self.options.get_option("colourscale"), index/len(self.data_processors))
            self.options.add_option("line", line)

            # Grab and plot data
            scatter = self.data_processors[lbl]
            self.fig.add_trace(go.Scatter(
                x=scatter.get_data(self.x_observable, *args, **kwargs),
                y=scatter.get_data(self.y_observable, *args, **kwargs),
                mode='lines',
                name=scatter.get_data('label'),
                line=line
            ))

        # Grab axis titles from last IVData if they have not yet been externally set
        if not self.titles_set:
            self.set_axes_titles(
                scatter.get_units(self.x_observable),
                scatter.get_units(self.y_observable)
            )
        self.fig.show(config=get_svg_config())
