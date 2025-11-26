from implementations.utils.plotly_colour_helpers.get_continuous_colour import get_continuous_colour
from implementations.utils.plotly_colour_helpers.get_discrete_colour import get_discrete_colour


def get_plotly_colour(colorscale, value):
    """
    Detect colourscale type based on structure.
    This function assumed discrete scales to be lists of colours and thus flat while continous scales are assumed to
    be a list of tuples containing some value and the associated colour.
    """
    # Determine if colorscale is continuous (nested list) or discrete (flat list)
    is_continuous = isinstance(colorscale[0], (list, tuple)) and len(colorscale[0]) == 2

    if is_continuous:
        return get_continuous_colour(colorscale, value)
    else:
        return get_discrete_colour(colorscale, value)