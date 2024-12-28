import plotly.colors


def check_and_covert_colour(color):
    """Convert a color from hex to RGB if needed."""
    # Deal with string formats
    if isinstance(color, str):
        if color.startswith('#'):
            # Check if the color is a hex value (starts with #)
            return plotly.colors.label_rgb(plotly.colors.hex_to_rgb(color))
        elif color.startswith('rgb'):
            # If the color is already in rgb/rgba format, return it as-is
            return color

    # If a tuple was given go ahead
    elif isinstance(color, tuple) and len(color) == 3:
        return color

    # Anything else not explicitly dealt with should raise an error
    else:
        raise ValueError(f"Unrecognized color format: {color}")


def get_continuous_colour(colorscale, value):
    """
    If a continuous colourscale is used then the value is a number that can be used to interpolate the colourscale.
    """
    if len(colorscale) < 1:
        raise ValueError("colorscale must have at least one color")

    if value <= 0 or len(colorscale) == 1:
        return colorscale[0][1]
    if value >= 1:
        return colorscale[-1][1]

    for cutoff, color in colorscale:
        color = check_and_covert_colour(color)
        if value > cutoff:
            low_cutoff, low_color = cutoff, color
        else:
            high_cutoff, high_color = cutoff, color
            break

    # noinspection PyUnboundLocalVariable
    return plotly.colors.find_intermediate_color(
        lowcolor=low_color, highcolor=high_color,
        intermed=((value - low_cutoff) / (high_cutoff - low_cutoff)),
        colortype="rgb")


def get_discrete_colour(colorscale, index):
    """
    If a discrete colourscale is used then the index could go out of bounds. Use modulo operator to wrap.
    """
    return colorscale[index % (len(colorscale))]


def get_colour(colorscale, value):
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