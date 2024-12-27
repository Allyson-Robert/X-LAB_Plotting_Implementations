from analysis.data.data_processors.data_processors import DataProcessor
from utils.plot_preppers.scatter_prep import scatter_prepper
from utils.plot_preppers.export_to_svg import get_svg_config
from analysis.plotters.plotter_options import PlotterOptions
from analysis.plotters.plotter import Plotter
from analysis.utils.get_colour import get_colour
import plotly.graph_objects as go
import plotly.colors


class ScatterDataPlotter(Plotter):
    def __init__(self, title, x_observable: str, y_observable: str, options: PlotterOptions):
        self.title = title
        self.fig = go.Figure()
        self.x_observable = x_observable
        self.y_observable = y_observable

        self.data_processors = None

        self.line = None
        self.colorscale = plotly.colors.get_colorscale("Viridis")
        self.titles_set = False
        expected_options = []
        for option in expected_options:
            try:
                options.get_option(label = option)
            except:
                raise ValueError("Invalid Options Object")

        self.options = options

    def ready_plot(self, data_processors: dict[str, DataProcessor], options: dict):
        self.fig = scatter_prepper(self.fig)
        self.fig.update_layout(
            title={'text': self.title},
            legend_title=options["legend_title"],
        )
        self.data_processors = data_processors

        # Define line properties
        if options["presentation"] or options["time_evolved"]:
            self.line = dict()

        if options["presentation"]:
            self.line["width"] = 5

        if options["time_evolved"]:
            self.colorscale = plotly.colors.get_colorscale("Magenta")

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
            if self.line is not None:
                self.line["color"] = get_colour(self.colorscale, index/len(self.data_processors))

            # Grab and plot data
            scatter = self.data_processors[lbl]
            self.fig.add_trace(go.Scatter(
                x=scatter.get_data(self.x_observable, *args, **kwargs),
                y=scatter.get_data(self.y_observable, *args, **kwargs),
                mode='lines',
                name=scatter.get_data('label'),
                line=self.line
            ))

        # Grab axis titles from last IVData if they have not yet been externally set
        if not self.titles_set:
            self.set_axes_titles(
                scatter.get_units(self.x_observable),
                scatter.get_units(self.y_observable)
            )
        self.fig.show(config=get_svg_config())
