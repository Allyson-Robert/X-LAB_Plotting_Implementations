import plotly.colors

from implementations.utils.plotly_colour_helpers.check_and_covert_colour import check_and_covert_colour


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
