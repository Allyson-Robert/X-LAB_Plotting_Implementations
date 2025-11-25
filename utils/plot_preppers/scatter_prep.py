import plotly.graph_objects as go


def scatter_prepper(fig: go.Figure) -> go.Figure:
    """
    Apply standard formatting to a Plotly scatter Figure.

    This helper function configures a scatter plot figure with a consistent
    visual style suitable for publication-quality plots and use within the
    X-LAB Plotting GUI. It adjusts title placement, font settings, axis
    appearance, and grid visibility.

    The following changes are applied:
    - Centers the main title and positions it slightly below the top of the figure.
    - Sets a uniform font family and size for the figure.
    - Formats x and y axes with visible outer lines, ticks on the outside, and
      no top/right spines.
    - Ensures axis ticks point outward and are clearly visible.
    - Removes all grid lines from both axes for a clean look.

    Parameters
    ----------
    fig : go.Figure
        A Plotly ``Figure`` instance containing scatter traces to be styled.

    Returns
    -------
    go.Figure
        The same ``Figure`` instance with updated layout and axes styling.
    """
    # Format title
    fig.update_layout(
        title={
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
    )

    # Format font
    fig.update_layout(
        font=dict(
            family="Open Sans",
            size=18,
            color="RebeccaPurple"
        ),
    )

    # Format background colours
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    # Format axes
    fig.update_xaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        ticks="outside"
    )

    fig.update_yaxes(
        showline=True,
        linewidth=2,
        linecolor='black',
        ticks="outside"
    )

    # No Grid
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    return fig
